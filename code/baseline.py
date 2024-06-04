import re
from collections import Counter
from itertools import islice, tee

import numpy as np
import spacy


class PlanSum:
    def __init__(self, data, data_type="pddl"):
        self.data = data
        self.data_type = data_type
        self.nlp = spacy.load("en_core_web_sm") if data_type == "recipe" else None

    @staticmethod
    def parse_data(data, data_type):
        parsed_data = []
        if data_type == "pddl":
            for plan in data:
                actions = [action.strip("()") for action in eval(plan)]
                parsed_data.append(actions)
        elif data_type == "recipe":
            for recipe in data:
                steps = recipe[0].split("\n")
                parsed_data.append(steps)
        elif data_type == "travel":
            for route in data:
                steps = route
                parsed_data.append(steps)
        return parsed_data

    @staticmethod
    def ngrams(lst, n):
        return zip(*(islice(seq, index, None) for index, seq in enumerate(tee(lst, n))))

    def analyze_text_view(self, parsed_data, ngram_size=3):
        all_items = []

        for item in parsed_data:
            all_items.extend(item)

        common_items = Counter(all_items)
        filtered_items = {item: freq for item, freq in common_items.items() if freq < 5}
        ngram_counter = Counter(self.ngrams(all_items, ngram_size))
        filtered_ngrams = {
            ngram: count for ngram, count in ngram_counter.items() if count < 5
        }

        return {
            "common_items": list(filtered_items.items())[:2],
            "ngrams": list(filtered_ngrams.items())[:2],
        }

    def analyze_plan_view(self, parsed_data):
        all_items = [
            item.split()[0] for item_list in parsed_data for item in item_list if item
        ]  # Only extract action/step names
        item_counts = Counter(all_items)
        most_common_items = item_counts.most_common(
            5
        )  # Get more than needed to ensure uniqueness later

        secondary_mentions = Counter()
        for item_list in parsed_data:
            for item in item_list:
                secondary = item.split()[
                    1:
                ]  # Extracting secondary parts (objects/ingredients) involved in actions/steps
                secondary_mentions.update(secondary)
        most_common_secondary = secondary_mentions.most_common(
            2
        )  # Only top 2 most involved objects/ingredients

        min_length_plan_index = min(
            range(len(parsed_data)), key=lambda i: len(parsed_data[i])
        )

        # Compute ngrams for the most common action sequences
        all_action_sequences = [
            seq for item_list in parsed_data for seq in self.ngrams(item_list, 3)
        ]
        action_sequence_counts = Counter(all_action_sequences)
        most_common_action_sequence = action_sequence_counts.most_common(1)

        return {
            "total_items": len(parsed_data),
            "avg_steps": np.mean([len(item_list) for item_list in parsed_data]),
            "step_range": [
                min([len(item_list) for item_list in parsed_data]),
                max([len(item_list) for item_list in parsed_data]),
            ],
            "most_common_items": most_common_items[
                :2
            ],  # Ensure only top 2 unique are returned
            "most_common_secondary": most_common_secondary,
            "shortest_plan_index": min_length_plan_index,
            "most_common_action_sequence": most_common_action_sequence,
        }

    def analyze_travel_view(self, parsed_data):
        road_mentions = Counter()

        for route in parsed_data:
            for step in route:
                road = self.extract_road_name(step)
                if road:
                    road_mentions.update([road])

        most_common_roads = road_mentions.most_common(5)  # Get top 5 most common roads
        min_length_route_index = min(
            range(len(parsed_data)), key=lambda i: len(parsed_data[i])
        )

        return {
            "total_items": len(parsed_data),
            "avg_steps": np.mean(
                [len(route) for route in parsed_data]
            ),  # Correct average steps calculation
            "step_range": [
                min([len(route) for route in parsed_data]),
                max([len(route) for route in parsed_data]),
            ],
            "most_common_roads": most_common_roads,
            "shortest_route_index": min_length_route_index,
        }

    @staticmethod
    def extract_road_name(step):
        # A simple extraction method based on patterns commonly found in step descriptions
        patterns = [
            r"onto (\w+\s+\d+)",  # Matches patterns like 'onto I 95' or 'onto US 1'
            r"onto (\w+\s+\w+)",  # Matches patterns like 'onto Main Street'
        ]
        for pattern in patterns:
            match = re.search(pattern, step)
            if match:
                return match.group(1)
        return None

    def generate_summary(self, text_view, item_view):
        if self.data_type == "travel":
            # Summarize the must-take roads
            must_take_roads = ", ".join(
                [
                    f"{road} ({count} times)"
                    for road, count in item_view["most_common_roads"]
                ]
            )
            shortest_route_index = item_view["shortest_route_index"]
            summary = (
                f"Analysis of {item_view['total_items']} travel routes reveals an average of {item_view['avg_steps']:.2f} steps per route. "
                f"Among these routes, the must-take roads are {must_take_roads}. The route with the least number of steps is Route: {shortest_route_index+1}."
            )
        else:
            if self.data_type == "pddl":
                unique_items = {}
                if "most_common_items" in item_view:
                    for item, count in item_view["most_common_items"]:
                        if item not in unique_items or unique_items[item] < count:
                            unique_items[item] = count
                    items_only = ", ".join(
                        [
                            f"{item} ({count} times)"
                            for item, count in unique_items.items()
                        ][:2]
                    )  # Taking only top 2

                secondary_only = ", ".join(
                    [
                        f"{secondary} ({count} times)"
                        for secondary, count in item_view.get(
                            "most_common_secondary", []
                        )
                    ]
                )
                shortest_plan_index = item_view["shortest_plan_index"]
                most_common_action_sequence = " -> ".join(
                    item_view["most_common_action_sequence"][0][0]
                )
                summary = (
                    f"Analysis of {item_view['total_items']} plans reveals an average of {item_view['avg_steps']:.2f} steps per plan, "
                    f"with most common actions - {items_only} and most involved objects - {secondary_only}. "
                    f"The plan with the least number of steps is Plan: {shortest_plan_index+1}. "
                    f"The most common action sequence is: {most_common_action_sequence}."
                )
            else:
                must_have_ingredients = ", ".join(
                    [
                        f"{item.strip()} ({count} times)"
                        for item, count in item_view.get("most_common_items", [])
                    ]
                )
                key_steps = ", ".join(
                    [
                        f"{action} ({count} times)"
                        for action, count in item_view.get("most_common_secondary", [])
                    ]
                )
                shortest_recipe_index = item_view["shortest_recipe_index"]
                summary = (
                    f"Analysis of {item_view['total_items']} recipes reveals an average of {item_view['avg_steps']:.2f} steps per recipe, "
                    f"with must-have ingredients - {must_have_ingredients}, and key actions - {key_steps}. "
                    f"The recipe with the least number of steps is Recipe: {shortest_recipe_index+1}."
                )

        return summary


# Choose the data type
data_type = "pddl"  # or 'travel' or 'recipe'

# Analyze the data
analyzer = PlanSum(data, data_type)
parsed_data = analyzer.parse_data(data, data_type)
text_view_summary = (
    analyzer.analyze_text_view(parsed_data, ngram_size=3)
    if data_type != "travel"
    else None
)
item_view_summary = (
    analyzer.analyze_plan_view(parsed_data)
    if data_type != "travel"
    else analyzer.analyze_travel_view(parsed_data)
)
print(analyzer.generate_summary(text_view_summary, item_view_summary))
