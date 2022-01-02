from flask import Flask, render_template
import json

from main import get_tweets
from sentiment import sentiment_analyser_score

app = Flask(__name__)


@app.route('/')
def display_chart():  # put application's code here
    title = 'Data Visualisation Project'
    description = 'Sentiment Visualisation Chart'

    df = get_tweets('johnny depp')

    pos, neu, neg = sentiment_analyser_score(df)

    labels = ['positive', 'neutral', 'negative']
    values = [pos, neu, neg]

    data = zip(labels, values)

    list2 = []

    for label, value in data:
        list2.append({'name': label, 'y': value})

    return render_template('chart-display.html', chart_title=title, description_txt=description, chart_name='column', data=list2)


if __name__ == '__main__':
    app.run(debug=True)
