from flask import Flask, request, render_template
import json
import pandas as pd
import pandas_highcharts.core

from main import get_tweets
from sentiment import sentiment_analyser_score
from visual import print_visual

app = Flask(__name__)


@app.route('/graph')
def display_chart(chart_id='chartid', chart_type='column', chart_height=600):  # put application's code here
    title = 'Data Visualisation Project'
    description = 'Sentiment Visualisation Chart'

    df = pd.read_csv('./output.csv', index_col='0', parse_dates=True)
    df = get_tweets('johnny depp')
    dataset = pandas_highcharts.core.serialize(df, render_to='chart', output_type='json')

    pos, neu, neg = sentiment_analyser_score(df)

    labels = ['positive', 'neutral', 'negative']
    values = [pos, neu, neg]

    data = zip(labels, values)

    list2 = []

    for label, value in data:
        list2.append({'name': label, 'y': value})

    return render_template('chart-display.html', chart=dataset, data=list2)


if __name__ == '__main__':
    app.run(debug=True)
    print_visual()
