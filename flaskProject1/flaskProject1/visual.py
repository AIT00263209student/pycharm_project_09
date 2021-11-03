import json

import matplotlib.pyplot as plt
import pandas as pd

# get output file and sort data
output = pd.read_csv('output.csv', names=['age', 'location', 'polarity'])
print(output.head())

# presenting data as a bar chart
fig, ax = plt.subplots()

# presenting data as a pie chart
