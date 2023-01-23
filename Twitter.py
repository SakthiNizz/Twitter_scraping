import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st
import pymongo

def mongo(df):    
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = client["twitter"]
    mycoll = mydb[f"{search}_tweet"]
    df.reset_index(inplace=True)
    data_dict = df.to_dict("records")
    mycoll.insert_one({"index":f"{search}","data":data_dict})
    st.success("Uploaded Successfully!",icon='✅') 
    st.balloons()
    collections = mydb.list_collection_names()
    st.write("List of collection that already exists : ")
    # for i in collections:
    st.write(collections)


tweets_list1 = []
with st.form("my_form"):
    default_since = '2020-06-01'
    default_until = '2020-07-31'
    search = st.text_input("Enter Text that you want to search : ")
    since = st.text_input('Enter the start_date :',default_since) 
    until = st.text_input('Enter the start_date :', default_until)
    maxTweets = st.slider('Enter the count :', 0,1000,100)
    maxTweets = int(maxTweets)
    summit = st.form_submit_button('Submit')
    if summit:
        passing = (f'{search} since:{since} until:{until}')
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(passing).get_items()):
            if i>maxTweets:
                break
            tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.url, tweet.replyCount,  tweet.retweetCount,tweet.lang, tweet.likeCount ])


tweets_df1 = pd.DataFrame(tweets_list1, columns=['DateTime', 'Tweet_ID', 'Content', 'User_Name', 'URL', 'Reply_count', 'Re_Tweet_Count','Language', 'Like_Count'])
st.write(tweets_df1)

with st.form("form"):
    st.write("Press Enter to upload dataset into DB : ")
    enter = st.form_submit_button("Enter")
    if enter:
        mongo(tweets_df1)
        
       
def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

csv = convert_df(tweets_df1)

st.download_button(
"Press to Download the Dataframe to CSV file format",
csv,
f"{search}_tweet.csv",
"text/csv",
key='download-csv'
)

def convert_json(df):
    return df.to_json().encode('utf-8')

json = convert_json(tweets_df1)
st.download_button(
"Press to Download the Dataframe to JSON file format",
json,
f"{search}_tweet.json",
"text/json",
key='download-json'
)