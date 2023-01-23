# Twitter_scraping
![images](https://user-images.githubusercontent.com/107666598/213983094-ebd2044e-2cef-4bd6-857c-40a49b1d56e5.jpeg)

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

# Working Procedure:

1. Download the "twitter.py" file.

2. Open Command Promt and Go to such directories using 'cd'![twt_cmd](https://user-images.githubusercontent.com/107666598/213982301-19f45089-b4ef-4708-8c2d-999a28d6c3e4.png)
3. The window that automatically get open in your browser. ![twt1](https://user-images.githubusercontent.com/107666598/213982432-571fa9e5-49e7-42d9-bd42-0d679eebea49.png)
4. You can perform search and can also modify since and until date and also the count and then 'Submit'. 
5. You can see...!![twt2](https://user-images.githubusercontent.com/107666598/213982627-ec903835-705d-4dc3-aadc-7ee72209fbe6.png)
6. You can also uploaded it in your Database![twt3](https://user-images.githubusercontent.com/107666598/213982711-6fc84e8f-e216-4dad-8ce0-c3659b7116a2.png)
7. You can also downloaded it!![twt4](https://user-images.githubusercontent.com/107666598/213982760-f5f01d2b-8f73-4c60-88ab-f36742146312.png)



Thanks for reading! 
