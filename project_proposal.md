# Understanding the declive of Venezuela by analyzing news from 1999 to present. 

For this project, I'll be using [The Guardian API](https://open-platform.theguardian.com/documentation/search) to retrieve bodies of text from news
articles (spanning more than 20 years of news articles, starting in 1999), and apply NLP techniques to do topic modeling over a determined timeframe, and see the changes over time, trying to develop an understanding of how the country economically plummeted. 

This is how a call to the API is done:
<img width="609" alt="Screen Shot 2021-12-08 at 5 22 33 PM" src="https://user-images.githubusercontent.com/34829066/145302105-8e879b1f-0d72-4634-bb93-5a4da9c51fc5.png">





And this is how a part of the result looks like:

<img width="996" alt="Screen Shot 2021-12-08 at 5 21 49 PM" src="https://user-images.githubusercontent.com/34829066/145302156-2b791d09-5178-48d8-a0c0-b53482585f54.png">

The MVP for this project will consists in creating a database to storage all of the news content (with the capacity of periodically adding articles to the database), 
do preprocessing and apply topic modeling.  



The end goal is to build a web app, where users could see the evolution of the news associated to the country, from 1999-to present times.  
