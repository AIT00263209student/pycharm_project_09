from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

text = 'Everything is crap'

analyser = SentimentIntensityAnalyzer()
blob = TextBlob(text)

print('Textblob output', blob.sentiment.polarity)


def sentiment_analyser_score(data):
    score = analyser.polarity_scores(data)
    print("{:-<40} {}".format(data, str(score)))


sentiment_analyser_score(text)