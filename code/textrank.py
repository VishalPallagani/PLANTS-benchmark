import networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

plans = [
    [
        "Head east",
        "Turn left onto Logan Street",
        "Turn left",
        "Turn left",
        "Turn right onto East 8th Avenue",
        "Turn left onto Grant Street",
        "Turn left onto East Speer Boulevard",
        "Turn right onto Logan Street",
        "Turn right onto East 3rd Avenue",
        "Turn left onto Broadway",
        "Turn left",
        "Keep left",
        "Keep left onto I 25 Express Lane, I 25 Express",
        "Keep right",
        "Keep right",
        "Turn left onto North 31st Street",
        "Keep right",
        "Turn sharp right onto Cave of the Winds Road",
        "Keep left onto Cave of the Winds Road",
        "Turn left",
        "Arrive at your destination, on the right",
    ],
    [
        "Head east",
        "Turn left onto Logan Street",
        "Turn left",
        "Turn left",
        "Turn right onto East 8th Avenue",
        "Turn left onto Grant Street",
        "Turn left onto East Speer Boulevard",
        "Turn right onto Logan Street",
        "Turn right onto East 3rd Avenue",
        "Turn left onto Broadway",
        "Turn left",
        "Keep left",
        "Keep right",
        "Keep left",
        "Keep right",
        "Keep right",
        "Keep right",
        "Turn left",
        "Keep left",
        "Keep right",
        "Keep right",
        "Turn left onto North 31st Street",
        "Keep right",
        "Turn sharp right onto Cave of the Winds Road",
        "Keep left onto Cave of the Winds Road",
        "Turn left",
        "Arrive at your destination, on the right",
    ],
    [
        "Head east",
        "Turn left onto Logan Street",
        "Turn left",
        "Turn left",
        "Turn right onto East 8th Avenue",
        "Turn left onto Grant Street",
        "Turn left onto East Speer Boulevard",
        "Turn right onto Logan Street",
        "Turn right onto East 3rd Avenue",
        "Turn left onto Broadway",
        "Turn left",
        "Keep left",
        "Keep right",
        "Keep left",
        "Keep right",
        "Keep right",
        "Keep right",
        "Turn left",
        "Turn left onto North Pinery Parkway",
        "Continue straight onto North Pinery Parkway",
        "Turn left onto South Parker Road, CO 83",
        "Keep left",
        "Keep right",
        "Keep right",
        "Turn left onto North 31st Street",
        "Keep right",
        "Turn sharp right onto Cave of the Winds Road",
        "Keep left onto Cave of the Winds Road",
        "Turn left",
        "Arrive at your destination, on the right",
    ],
]
unique_actions = list(set(action for plan in plans for action in plan))

# Create a graph
G = nx.Graph()

# Add nodes
for action in unique_actions:
    G.add_node(action)

# Vectorize the actions for similarity measurement
vectorizer = TfidfVectorizer()
action_vectors = vectorizer.fit_transform(unique_actions)

# Add edges between similar actions based on cosine similarity
for i in range(len(unique_actions)):
    for j in range(i + 1, len(unique_actions)):
        similarity = cosine_similarity(action_vectors[i], action_vectors[j])
        if similarity > 0.2:  # Threshold for similarity
            G.add_edge(unique_actions[i], unique_actions[j], weight=similarity[0, 0])

# Apply the TextRank algorithm
ranks = nx.pagerank(G)

# Sort actions by rank
sorted_actions = sorted(ranks, key=ranks.get, reverse=True)

# Print the top-ranked actions as the summary
print(
    sorted_actions[:6]
)  # Adjust the number of actions based on your summary length constraint
