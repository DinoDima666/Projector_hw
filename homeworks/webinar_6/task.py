# Create a module plotter.py that takes a list of numbers as input and uses matplotlib to generate a line plot.
# Generate a graph for the UAH/USD exchange rate since 2000.

from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import csv


dates = []
rates = []



with open("target.csv") as file:
    reader = csv.DictReader(file, fieldnames=["Date","Rate","High (est)","Low (est)"])

    next(reader)
    for row in reader:
        dates.append(datetime.strptime(row["Date"], '%Y-%m-%d'))
        rates.append(float(row["Rate"]))

plt.style.use('_mpl-gallery')
# plot
fig, ax = plt.subplots()
ax.plot(dates, rates, linewidth=2.0)
plt.show()