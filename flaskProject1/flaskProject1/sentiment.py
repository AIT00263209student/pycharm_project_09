from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import pandas as pd
import time
import csv

df = pd.read_csv('output.csv')
df.head()

analyser = SentimentIntensityAnalyzer()
blob = TextBlob(df)

print('Textblob output', blob.sentiment.polarity)


def sentiment_analyser_score(data):  # get and print polarity for tweet data
    score = analyser.polarity_scores(data)
    print("{:-<40} {}".format(data, str(score)))


def data_drill_down(data):  # obtain drill-down info on tweet data
    df2 = pd.DataFrame()
    df2['id'] = df['id'].values
    df2['user.screen_name'] = df['user.screen_name'].values
    df2['user.age'] = df['user.age'].values
    df2['place.country'] = df['place.country'].values
    df2['tweet'] = df['text'].values

    header = ['id', 'user.screen_name', 'user.age', 'place.country', 'tweet']
    df.to_csv('output2.csv', columns=header)


if __name__ == '__main__':
    sentiment_analyser_score(df)
    data_drill_down(df)