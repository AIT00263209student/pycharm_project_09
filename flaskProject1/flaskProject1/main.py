import tweepy as tp
from tweepy.auth import AuthHandler
import pandas as pd
from textblob import TextBlob


API_KEY = 'qyfDNcM65yeEp5cnwfDLho1oI'
API_SECRET = 'nOowF0lDLGdpNPby09FZebPUdBExViNnHf7tw7Fif3MQ68hN3U'
ACCESS_TOKEN = '1440589525424623629-H19obkwQo8b3KuQc3DPfDTptoeDARB'
ACCESS_SECRET = 'IcTUsG52XwDA3lG196P13ALJ89IzeSdXempofuSInS7YO'

# authentication
auth = tp.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tp.API(auth)


# get tweets containing a specific keyword
def get_tweets():
    tweets = api.search_tweets(q='Johnny Depp', lang="en")
    list = []


# print tweets
    for tweet in tweets:
        print(tweet)

    # sentiment analysis
        sentiment = TextBlob(tweet.text).sentiment.polarity

        if sentiment > 0.15:
            sentiment = 'positive'
        elif sentiment < -0.15:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'

        list.append((tweet.text, sentiment))

    df = pd.DataFrame(list)

    df.to_csv("output.csv", sep=",") # print to .csv file


if __name__ == '__main__':
    get_tweets()