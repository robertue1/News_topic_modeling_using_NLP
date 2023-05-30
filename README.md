# Understanding Venezuela's Crisis 
### 22 years of news articles ([The Guardian](https://www.theguardian.com/us)) analyzed using NLP

## Abstract

Venezuela was once one of the most developed countries in the Latin America region, thanks to being the country with the biggest oil reserves in the world,
and its priviliged geographical location. Today, the country is going through its worse crisis, and is generating a massive wave of migrants, most of them traveling
south in the continent. The idea of this project was to perform topic modeling on more than 7000 news articles from The Guardian, starting from 1999 to the present, and determine which were the key factors that led to this crisis unwinding. 


## Design

Initially, 7400 news articles were gathered by using The Guardian API, looking for the following keywords anywhere in the article: ('Venezuela,' 'Chavez' (late president), and 'Maduro' (current president)). After performing the pre-processing necessary to apply topic modeling technique, the resulting topics would not provide much information to help understand the country's current situation; for this reason, articles were filtered to include those with the keywords as part of the title. Results from the modeling and a database were uploaded to a public GitHub repository, a connection to Streamlit Share was established, and an interactive web app was deployed, where users can do their research by looking at articles titles and their links stored in the database serving the project.

## Data

News articles from [The Guardian API](https://open-platform.theguardian.com/documentation/search), including title, link, date, category, and the entire content of the article (in HTML format). The articles added up to more than 7000 and the time span is from 1999 to present times. 

## Tools 

* Google Colab - Processing platfrom
* Requests - Data Acquisition
* Pandas, NumPy - Processing and data exploration
* Gensim, NTLK, Scikit-Learn - NLP pre-processing and model development. 
* SQLite and Github- Data storage
* Streamlit - Web app design and deployment

## Communication 

5 minutes presentation, a slide deck and a publicly available [web application](https://share.streamlit.io/robertue1/news_topic_modeling_using_nlp/main/app.py)


