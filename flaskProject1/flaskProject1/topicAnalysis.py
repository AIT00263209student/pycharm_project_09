from flask import Flask, request
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


@app.route('/single_topic', methods=['GET', 'POST'])
if request.method == 'POST':
    text = request.form('text')
    data = text.upper()
# get tweets containing a specific keyword
    tweets = api.search_tweets(q=data, lang="en")
    list = []


# print tweets
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


if __name__ == '__main__':
    app.run(debug=True)