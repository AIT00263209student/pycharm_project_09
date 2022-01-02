import json
from flask import Flask, render_template

import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)


@app.route('/print_visual')
def print_visual():
    # get output file and sort data
    output = pd.read_csv('output.csv', names=['age', 'location', 'polarity'])
    print(output.head())

    # presenting data as a bar chart
    fig, ax = plt.subplots()
    return render_template('chart-display.html', print_visual=plt.subplots() )

    # presenting data as a pie chart


if __name__ == '__main__':
    app.run(debug=True)