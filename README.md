# Twitter_scraping

  Here is an amazing script with streamlit GUI to scrape datas from twitter. This mainly helps for data Scientist to research and scrape data from twitter.
  
 # Benifits:
  
    1. You can Search your needs
    
    2. You can view those search datas
    
    3. You can Store data into collection in mongo db
    
    4. You can download such data into csv or json file format throughout yours needs.
    
# Discription:
# Problem Statement:
  Today, data is scattered everywhere in the world. Especially in social media, there may be a big quantity of data on Facebook, Instagram, Youtube, Twitter, etc. This consists of pictures and films on Youtube and Instagram as compared to Facebook and Twitter. To get the real facts on Twitter, you want to scrape the data from Twitter. You Need to Scrape the data like (date, id, url, tweet content, user,reply count, retweet count,language, source, like count etc) from twitter.
  
# Approach: 
  ●	By using the “snscrape” Library, Scrape the twitter data from Twitter
  
  ●	Creating a dataframe with date, id, url, tweet content, user,reply count, retweet count,language, source, like count.
  
  ●	Storing each collection of data into a document into Mongodb along with the hashtag or key word we use to  Scrape from twitter.
  
  ●	Creating a GUI using streamlit that should contain the feature to enter the keyword or Hashtag to be searched, select the date range and limit the tweet count need to be scraped. After scraping, the data needs to be displayed in the page and need a button to upload the data into Database and download the data into csv and json format.
