# Choose a dataset, you can use Seaborn example datasets. 
# Create a cheat sheet for yourself containing all plot types discussed in the lecture.
# Provide the following info:  
#   - Plot type 
#   - Use cases (categorical data, distribution, etc.) 
#   - Example on the dataset

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# print(tips.tail(3))

# Data disctibution plots. Used to show the data disctributions for chosen parameters. We can discplay this data by default in a gistogram.
# Also we can pass this data into a "kde" gistogram to smooth out visualisation to see the curve

# sns.displot(tips, x ='tip', kind='kde')  
# plt.show()

# Regression plots can be used to show the correlation between two parameters from the dataset we want to analyze.

# _ = sns.regplot(x = "total_bill", y = "size", data=tips)
# plt.show()

# Other types

# We use CATEGORIAL PLOTS to represent data which is not an integer or a float and represent some kind of characteristic as a string.
# Stripplot is going to be defaul diagram type for this type of plot

# _ = sns.catplot(x = "tip", y = "sex", data= tips)
# plt.show() 

# Distribution plots are best for visualization of the spread of data.
# Types of diagrams used are "box" and "violin", can be combined for a better visualization

# _ = sns.catplot(x="day", y="total_bill", hue="smoker", kind="box", data=tips)
_ = sns.catplot(x="tip", y="sex", hue= "smoker", kind="violin", orient="h", data=tips)
plt.show() 







