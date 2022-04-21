# Hyper-News [Graph For All Million Dollar Challenge]

## Problem Statement : Reduce The Noise Of News Search

#### Author: Ashleigh Faith, Director, Knowledge Graph and Semantic Search at EBSCO

Google, while a wonderful resource for quick-fix questions, starts to repeat search results after the third page, this is especially true for news articles. A big reason for this is duplicate resources from common sister agencies like Associate Press and all the newspapers that use its articles, as well as reshares or reposts, artificially inflate the volume of an article/post and its importance. Re-posts or re-shares often are also changed slightly so Google does not see them as duplicates. This causes inflated importance of some posts (going “viral” unnecessarily) and gives a noisy Google search experience that may be hiding more relevant news articles from end-users.

### The Challenge
How can news articles with the same content be identified and associated with each other in order to prevent inflation of information importance? Take cues from copyright detection or song recognition as you design your solution. Attempt to identify duplicate news articles that you might scrape from Google or internet search results and what sources those articles commonly come from. How can this information be used to better enable the public to make sure they're getting the most important and diverse information?

### Approach

The desired state would likely be to have a hyper-node graph that represents the common metadata for a cluster of duplicate or near-duplicate articles/posts and how their metadata relates to one another. The individual articles and their metadata would be clustered together as relations to the hyper-node. Each hyper-node would in effect represent all versions of the individual articles and posts that are duplicates and give a normalized representation of the article/post. This hyper-node and its metadata can then be used to group articles/posts together in a search application to minimize noisy search for news articles/posts and help end-users identify if an article/post is actually 'going viral' or just overhyped and not worth their time. 

### Solution
* To scope this solution, we have taken a mix of news articles and posts and created a hypergraph of as many duplicate 
* Documented the metadata for each article/post in your dataset, assess the metadata for duplicate information to create a similarity score, the most similar articles/posts will create the cluster of articles/posts related to each hyper-node. 
* Threshold for similarity is 75% (0.75 f-score) 
* Documented the normalized information (the data the clustered articles/posts have in common) as metadata for the hyper-node and the similarity between each hyper node. 
* Represented the similarity of metadata between hyper-nodes that allows for the solution to scale so that as new news articles/posts are posted, the metadata can be queried to identify if the new article/post is an existing duplicate, or a new article/post.

### The Desired State 
* The first is the model and its populated hyper-graph 
* The second is the similarity model, likely a machine learning model (Bert). 
* Each hyper-node has the normalized metadata of the articles it represents, as well as the similarity score for the individual articles to one another and the similarity score between each hyper-node. 
* The machine learning model is open-sourced and flexible enough to be pointed at any news or text based dataset.

### Access Solution
Refer to the [Colab Notebook](https://colab.research.google.com/drive/11fLqhvOJ1A5juGGS_Mhzwj2ziSNuqN5_?usp=sharing)

The notebook has each step mentioned in detail and how we utilise tigergraph and gsql to scale our solutions

You can also refer to [This PDF](solution.pdf) for more information on how our solution is
- Impactful in solving a real world problem 
- Innovative use case of graph
- Ambitious and complex graph
- Applicable graph solution 

Other additions: 

 - **Data**: Refer to [README.md](news-corpus/README.md) to create your own database 
 - **Technology Stack**: Python, Machine Learning, GSQL, Tigergraph, Javascript 
 - **Demo**: Watch [Here](https://youtu.be/leLlgDcjXKM)
 - **PPT**: [Google Slides](https://docs.google.com/presentation/d/13lDwYo54N-C5wIRGGjjBZR3HopzHFZlB_SLWcOG5dEk/edit?usp=drivesdk)

### Installation

Please give detailed instructions on installing, configuring, and running the project so judges can fully replicate and assess it. 

This can include:
1. Clone repository
2. Install dependencies
```
pip install -r requirements.txt
```
3. Replicate [Colab Notebook](https://colab.research.google.com/drive/11fLqhvOJ1A5juGGS_Mhzwj2ziSNuqN5_?usp=sharing) with your own data

###  References

* [Devpost](https://devpost.com/software/hyper-news?ref_content=my-projects-tab&ref_feature=my_projects)
* [Documentation](https://docs.tigergraph.com/home/)

### Contributors

* **Vidhi Gupta :** gvidhi9@gmail.com
* **Deep Rodge :** deeprodge14@gmail.com
