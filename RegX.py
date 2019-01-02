import tweepy
import csv
import pandas as pd
import json
from tweepy import Stream
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener
import time
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import regex
import pandas as pd

consumer_key = 'D5N8B0YT1CUq9MRrzpQ7w7tZP'
consumer_secret = '46p2fGkQFPQsxNT8xBG1DJCbddBcoHMkHyqaBbNNfvoqOeRSaE'
access_token = '1720598647-uJRKmu80bCXmqerxroKcM0DM2DKzuVqrrlsKrf9'
access_token_secret = 'pQvA4EwJj79FiElLkYpn3Kl8RJ1wT9ZNmOr9YadSUDvu8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

siaObject = SentimentIntensityAnalyzer()

# Open/Create a file to append data
csvFile = open('Starbucks3.csv', 'w', encoding='utf8')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#Starbucks",count=100,
                           lang="en",
                           since="2018-11-18").items():

    cleanString1 = regex.sub('[^A-Za-z]+', ' ', tweet.text)
    cleanString2 = cleanString1.split("http")[0]

    if (siaObject.polarity_scores(tweet._json['text'])['compound']) >= 0.05:

        csvWriter.writerow([tweet.created_at, cleanString2, tweet.user.location,'1', tweet.user.followers_count, tweet.user.description, tweet.retweet_count])
    elif (siaObject.polarity_scores(tweet._json['text'])['compound']) <= -0.05:

        csvWriter.writerow([tweet.created_at,cleanString2, tweet.user.location,'-1', tweet.user.followers_count, tweet.user.description, tweet.retweet_count])
    else:
        csvWriter.writerow([tweet.created_at,cleanString2, tweet.user.location,'0', tweet.user.followers_count, tweet.user.description,tweet.retweet_count])
    #print (tweet.created_at, tweet.text, tweet.user.location)


print(tweet)
