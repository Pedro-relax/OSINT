#imports for packages
import praw
import tweepy as tw
import pandas as pd
from tkinter import *

#to call tkinter
window=Tk()

#Title of dashboard
ds=Label(window, text="Data Scrapper", fg='#000000', font=("Georgia",16))
ds.place(x=175, y=10)

#function for button of twitter
def twi():
    #using twippy as the api wrapper with twitter account
    consumer_key = "HV6A7sHi7w9ewWSTIR59IKvrw"
    consumer_secret = "8GaPCii3KELlXBEF016uy8D4pP850vGycRvpaUmyuGBy2ooc1L"
    access_token = "1455544901647708177-Rvhi6a3Q3KKRYPolU43iTDoq26lhKi"
    access_token_secret = "JKzCRiXAKaiA0BPzjuNu4URoR6TrmVJrFiJTBzCNczu5h"
    bearer_token="AAAAAAAAAAAAAAAAAAAAAGFwWAEAAAAAuPWV3%2BqRbyLPBN5Ih2v%2F3sKZkGo%3DAKZt5CFmrq0gaOputzbUHlx5xtN0lr55VQNwStZdudMEzHBGn0"
    # authenticate
    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    # filter tweets
    search_query = "#sports -filter:tweets"

    twit_dict = {"id":[],"source":[], "created_at":[], "text":[], "location":[], "follower_count":[], "favorite_count ":[], "retweet_count":[],}
    # get tweets from the API
    for tweet in tw.Cursor(api.search_tweets, q=search_query, lang="en").items(100):
        twit_dict["id"].append(tweet.id)
        twit_dict['source'].append(tweet.source)
        twit_dict["created_at"].append(tweet.created_at)
        twit_dict["text"].append(tweet.text)
        twit_dict["location"].append(tweet.user.location)
        twit_dict["follower_count"].append(tweet.user.followers_count)
        twit_dict["favorite_count "].append(tweet.favorite_count)
        twit_dict["retweet_count"].append(tweet.retweet_count)
        
    # write dict to csv file for data analysis with Pandas  
    tweets_df = pd.DataFrame(twit_dict)
    tweets_df.to_csv('twitter.csv')

#twitter button        
twit=Button(window, text= "Twitter",fg='#00ACEE', bg='#FFFFFF', height=2, width=10,command=twi, font=("Arial",12))
twit.place(x=125, y=100)

#function for button for reddit
def re():
    #using praw as the api wrapper with new reddit account
    reddit = praw.Reddit(client_id='NmL51WH5zj9JdWeXEyKiMw',
                     client_secret='13NDkh83S65Yg_pDGFlWMxdjIhFK-g',
                     username='OsintAccount',
                     password='!Passw0rd7!',
                     user_agent='webscrapper')
    
    # set chosen subreddit to sports
    sub = reddit.subreddit("sports")
    # top 100 in hot
    hot_sub = sub.hot(limit=100)
    # dictionary to store data
    data_dict = {"id":[], "subreddit":[], "upvotes":[], "flair":[], "title":[], "url":[], "comms_num":[], "body":[]}
    # for each submission store data into
    for submission in hot_sub:
        data_dict["id"].append(submission.id)
        data_dict['subreddit'].append(submission.subreddit)
        data_dict["upvotes"].append(submission.score)
        data_dict["flair"].append(submission.link_flair_text)
        data_dict["title"].append(submission.title)
        data_dict["url"].append(submission.url)
        data_dict["comms_num"].append(submission.num_comments)
        data_dict["body"].append(submission.selftext)
    # write dict to csv file for data analysis with Pandas    
    data = pd.DataFrame(data_dict)
    data.to_csv('reddit.csv')

#reddit button
red=Button(window, text= "Reddit",fg='red', bg='#808080', height=2, width=10,command=re, font=("Arial",12))
red.place(x=280, y=100)

#Display for the GUI and its designs
window.configure(bg='#FFFFFF')
window.title('Data Scrapper')
window.resizable(0,0)
window.geometry("500x250")
window.mainloop()

