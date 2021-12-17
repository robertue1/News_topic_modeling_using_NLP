# Understanding Venezuela's Crisis 
### 22 years of news articles ([The Guardian](https://www.theguardian.com/us)) analyzed using NLP

## Abstract

Venezuela was once one of the most developed countries in the Latin America region, thanks to being the country with the biggest oils reserves in the world
and its priviliged geographical location. Today, the country is going through its worse crisis and is generating a massive wave of migrants, most of them traveling
south in the continent. The idea of this project, was to perform topic modeling on more than 6000 news articles from The Guardian, starting from 1999 to present times, and determine which where the key factors that lead to this crisis to unwind. 


## Design

Initially, 7400 news articles were gather by using The Guardian API, using the keywords: ('Venezuela', 'Chavez' (late president), 'Maduro' (current president)). After performing cleaning and pre-processing of the data to apply topic modeling. Topics weren't that useful to understand the current situation, for this reason, articles were filtered to only those that included any of the keywords in the title. Results from the modeling and a db were uploaded to a public GitHub repository, a connection to Streamlit Share was established and an interactive web-app was deployed, were users can do their own research, by looking at articles titles and their links stored in the database serving the project. 


## Data

News articles from [The Guardian API](https://open-platform.theguardian.com/documentation/search), including title, link, date, category and the entire content of the article (in HTML format). The articles added up to more than 7000 and the time span is from 1999 to present times. 

## Tools 

Google Colab - Processing platfrom
Requests - Data Acquisition
Pandas, numpy - Processing and data exploration
Gensim, NTLK, Scikit-Learn - NLP pre-processing and model development. 
SQLite and Github- Data storage
Streamlit - Web app design and deployment

## Communication 

5 minutes presentation, a slide deck and a publicly available [web application](https://share.streamlit.io/robertue1/engineering/main/app.py)


