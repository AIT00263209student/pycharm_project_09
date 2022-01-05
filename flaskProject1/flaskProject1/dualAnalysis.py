from flask import Flask, request
import tweepy as tp
from tweepy.auth import AuthHandler
import pandas as pd
from textblob import TextBlob
from visual import print_visual


API_KEY = 'qyfDNcM65yeEp5cnwfDLho1oI'
API_SECRET = 'nOowF0lDLGdpNPby09FZebPUdBExViNnHf7tw7Fif3MQ68hN3U'
ACCESS_TOKEN = '1440589525424623629-H19obkwQo8b3KuQc3DPfDTptoeDARB'
ACCESS_SECRET = 'IcTUsG52XwDA3lG196P13ALJ89IzeSdXempofuSInS7YO'

# authentication
auth = tp.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tp.API(auth)

app = Flask(__name__)

@app.route('/dual-analysis', methods=['GET', 'POST'])
if request.method == 'POST' && request.form.items(multi=True):
    text1 = request.form('text1')
    data1 = text1.upper()
    text2 = request.form('text2')
    data2 = text2.upper()

# get tweets containing a specific keyword
    tweets1 = api.search_tweets(q=data1, lang="en")
    tweets2 = api.search_tweets(q=data2, lang="en")
    list = []


# print tweets
    for tweet in tweets1:

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


if __name__ == '__main__':
    app.run(debug=True)
    print_visual()