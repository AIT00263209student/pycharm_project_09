import tweepy as tp
from tweepy.auth import AuthHandler
import pandas as pd
from textblob import TextBlob

API_KEY = 'pUgp871tte5LCyU33BX9MW04t'
API_SECRET = 'wd2dzPj4JJ6hAx0XNOryKQFrnDBf8PhPwdRv3PHlz4nkSyF87h'
ACCESS_TOKEN = '1440589525424623629-hp8Bal0aXxlqLmyo85ZVo0Afg3mYnO'
ACCESS_SECRET = 'rM6Qayp9m0Mfw0AvdY1kCsYrlahTsBOU1AqyH6VxFyPXg'

import tweepy as tp

auth = tp.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tp.API(auth)

tweets = api.search(q='Johnny Depp')

list = []

for tweet in tweets:

    sentiment = TextBlob(tweet.text).sentiment.polarity

    if sentiment > 0.15:
        sentiment = 'positive'
    elif sentiment < -.15:
        sentiment = 'neg'
    else:
        sentiment = 'neu'

    list.append((tweet.text, sentiment))

df = pd.DataFrame(list)

df.to_csv("output.csv", sep=",")
