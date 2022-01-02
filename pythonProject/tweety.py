import tweepy as tp
from tweepy.auth import AuthHandler
import pandas as pd
from textblob import TextBlob

API_KEY = 'qDe68hSUsvmYRqXlb5KAHmIT0'
API_SECRET = '1tKTQYRYu214pN4AvmJLwWZLgUB5LRsxMJfEu3HvXdaCNs2UuN'
ACCESS_TOKEN = '1440589525424623629-0M5CfzTaeT28Ek5Sz8pTibZx7pjMVP'
ACCESS_SECRET = 'HjhakwH3iS2mlrrA9albWmqkRtnq7zNrj0CGlvl0p2xH9'

import tweepy as tp

auth = tp.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tp.API(auth)

tweets = api.search_tweets(q='Johnny Depp', lang="en")
tweets2 = api.search_tweets(q='Amber Heard', lang='en')
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

    for tweet2 in tweets2:

        sentiment = TextBlob(tweet.text).sentiment.polarity

        if sentiment > 0.15:
            sentiment = 'positive'
        elif sentiment < -.15:
            sentiment = 'neg'
        else:
            sentiment = 'neu'

        list.append((tweet2.text, sentiment))

df = pd.DataFrame(list)

df.to_csv("output.csv", sep=",")
