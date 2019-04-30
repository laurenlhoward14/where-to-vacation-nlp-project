# I need a vacation! But where should I go?
Everyone's idea of the perfect vacation is different! Therefore, the goal of this project was to build a recommendation system to suggest where someone should vacation based on their personal interests. I scraped data from over 180 articles each summarizing what do in a place when you only have 36 hours to spend there. Using natural language processing and topic modeling techniques such as TF-IDF : Term Frequency — Inverse Document Frequency & NMF: Non-Negative Matrix Factorization I deciphered 6 main topics discussed across the corpus of articles. I then weighted the prevalence of each topic in each article in order to match places against an individual's preference in what they look for in a vacation. I then used to Flask to build an interface for a user to easily interact with the recommendation system.

**Tools:**

- Web Scraping (Beautiful Soup, Selenium)
- Non Relational Database to store and interact with data (MongoDB, pymongo)
- Python (Pandas, Sklearn, Seaborn)
- NLP Techniques (CountVectorizer, TfidfVectorizer)
- Topic Modeling & Dimensionality Reduction Techniques (NMF, TruncatedSVD, PCA, cosinesimilarity)
- Recommendation System Interface (Flask)

**Repository Includes:**

- Jupyter Notebook of full project process
- Modules including developed functions for the process & raw data used for scraping
- Video Demonstration of Flask App Recommender
- HTML & CSS code used to design the Flask App

[Please find the corresponding blog post here](https://medium.com/datadriveninvestor/i-need-a-vacation-but-where-should-i-go-b2ccdb0c8ebf)
