# Datasheet for dataset "PLANTS"

Questions from the [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) paper, v7.

Jump to section:

- [Motivation](#motivation)
- [Composition](#composition)
- [Collection process](#collection-process)
- [Preprocessing/cleaning/labeling](#preprocessingcleaninglabeling)
- [Uses](#uses)
- [Distribution](#distribution)
- [Maintenance](#maintenance)

## Motivation

### For what purpose was the dataset created? 

The PLANTS dataset was created for the novel task of plan summarization, which aims to generate concise summaries of action sequences that achieve specific goals, thereby facilitating quick understanding and decision-making. The authors identified a gap in the existing summarization literature, which has primarily focused on static documents and overlooked dynamic tasks involving sequences of actions, such as workflows, recipes, dialogs, and travel plans. The dataset was designed to address this gap and reinvigorate research in summarization, which some consider a solved problem.

### Who created the dataset and on behalf of which entity?
The dataset was created by Vishal Pallagani and Biplav Srivastava, who are affiliated with the AI Institute at the University of South Carolina.

### Who funded the creation of the dataset? 
There is no funding source for the creation of the PLANTS dataset.

## Composition

### What do the instances that comprise the dataset represent?

The instances represent multiple plans to achieve a goal across three categories of planning-like tasks - automated plans (e.g. for intelligent agents), recipes (e.g. cooking cheese sandwich), and travel routes (e.g. driving from Manhattan to Pleasantville).

### How many instances are there in total (of each type, if appropriate)?
There are a total of 30 instances, 10 per each category of the planning-like tasks (automated plans, recipes, and travel routes). Each instance from the automated plans and recipes category has 5 plans, whereas travel routes have 3 plans. Thus, a total of 130 distinct plans are captured in the dataset.

### Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?

Yes, the dataset contains all instances used for benchmark evaluation. The authors also release the generators for the planning-like tasks to create a bigger dataset in the future.

### What data does each instance consist of? 

Each instance has a category, domain, goal, and plans. The category represents the type of planning-like task, the domain (applicable only for automated plans) represents the planning environment with constaints, goal represents the aim of the task, and plan captures different possible plans to achieve the goal. All the instances are represented in text. 

### Is there a label or target associated with each instance?

No, there is no label or target associated with each instance.

### Is any information missing from individual instances?

The dataset does not contain gold plan summaries for each instance as it is challenging to obtain authoritative summaries for planning-like tasks due to their inherent variability and subjective nature.

### Are relationships between individual instances made explicit?

Yes, the plans are for achieving the goal of a particular planning-like task.

### Are there recommended data splits (e.g., training, development/validation, testing)?

Not applicable.

### Are there any errors, sources of noise, or redundancies in the dataset?

No, the dataset being small has been manually verified to check for errors if any.

### Is the dataset self-contained, or does it link to or otherwise rely on external resources?

There is a dependeny on Recipe1M+ dataset to obtain the ingredients and step-by-step instructions for select recipes.

### Does the dataset contain data that might be considered confidential?

No.

### Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?

No.

### Does the dataset relate to people? 

No.

## Collection process

### How was the data associated with each instance acquired?

The data is directly observable (raw text).

### What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software program, software API)?

For automated plans, SymK planner was used to generate 5 plans per planning problem written in PDDL. For recipes, the authors manually extracted multiple plans to cook a dish from Recipe1M+ dataset. For travel routes, OpenStreetMap API was used.

### If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?

The dataset is not a sample from a larger set.

### Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?

The data collection process is automated.

### Over what timeframe was the data collected?

The dataset was collected from May 10, 2024 to May 15, 2024.

### Were any ethical review processes conducted (e.g., by an institutional review board)?

No, this dataset did not have any sensitive information or human subjects for curation.

### Does the dataset relate to people?

No.

## Preprocessing/cleaning/labeling

### Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?

Multiple plans that achieve a common goal are represented as a list of lists. No additional preprocessing, cleaning, or labeling of the text data was performed as it was not necessary for our purposes.

### Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?

The raw dataset is present in the dataset.

### Is the software used to preprocess/clean/label the instances available?

No preprocessing/cleaning/labeling has been used.

## Uses

### Has the dataset been used for any tasks already?

Yes, the dataset has been used for planning task summarization, which involves generating a concise summary of multiple plans that achieve the same goal.

### Is there a repository that links to any or all papers or systems that use the dataset?

Yes, the authors have created a [GitHub](https://github.com/VishalPallagani/PLANTS-benchmark) repository to actively release information related to the task of plan summarization.

### What (other) tasks could the dataset be used for?
The dataset is only applicable for the task of plan summarization.

### Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?

No.

### Are there tasks for which the dataset should not be used?

The dataset is not fit for any tasks other than plan summarization.

## Distribution

### Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created? 

Yes, the dataset is open-sourced and available for research purposes. It is distributed under a Creative Commons (CC) license, allowing third parties to access and use it in accordance with the license terms.

### How will the dataset will be distributed (e.g., tarball on website, API, GitHub)?

The dataset is distributed on GitHub at [GitHub](https://github.com/VishalPallagani/PLANTS-benchmark) and is available for research purposes. It is also archived and citable with a DOI through Zenodo: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.11473815.svg)](https://doi.org/10.5281/zenodo.11473815).

### When will the dataset be distributed?
The dataset is open-sourced on June 04, 2024.

### Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?

The dataset is distributed under a Creative Commons (CC) license.

### Have any third parties imposed IP-based or other restrictions on the data associated with the instances?

No.

### Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?

No.

## Maintenance

### Who is supporting/hosting/maintaining the dataset?

The dataset is hosted for free on GitHub. It is maintained by the authors, who ensure that it is kept up-to-date and accessible for research purposes.

### How can the owner/curator/manager of the dataset be contacted (e.g., email address)?

Any details or queries regarding the dataset can be addressed to vishalp@mailbox.sc.edu.

### Is there an erratum?

There are no known errors or corrections related to the dataset at this time. If any errata are identified in the future, they will be documented and accessible through the GitHub repository.

### Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)?

We plan to release a newer version of the dataset in the future with more instances and gold summaries.

### If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were individuals in question told that their data would be retained for a fixed period of time and then deleted)?

No, the dataset does not relate to people.

### Will older versions of the dataset continue to be supported/hosted/maintained?

Yes, all versions of the dataset will be archived on Github as well as Zenodo.

### If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?

Yes, the dataset is designed to be extensible. Researchers and developers can use the provided generators to create additional instances or add new planning-like tasks. Contributions can be made by forking the GitHub repository, making the desired changes, and submitting a pull request. We encourage the community to collaborate and enhance the dataset, ensuring it remains a valuable resource for ongoing research.
