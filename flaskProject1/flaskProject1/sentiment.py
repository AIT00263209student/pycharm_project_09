from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import pandas as pd
import csv

df = pd.read_csv('output.csv')
df.head()

analyser = SentimentIntensityAnalyzer()
blob = TextBlob(df)

print('Textblob output', blob.sentiment.polarity)


def sentiment_analyser_score(data):
    score = analyser.polarity_scores(data)
    print("{:-<40} {}".format(data, str(score)))


if __name__ == '__main__':
    sentiment_analyser_score(df)