# Example 4.3
# Program to draw Pie Chart
# Import Libraries
import matplotlib.pyplot as plt
# %matplotlib inline
# Specify Data
labels = ["Raw Materials","Labour","Rent","Electricity"]
values = [30,90,30,30]
colors = ['b','g','r','c']
explode = (0.05,0.05,0.05,0.05)
# Draw a Pie Chart
plt.pie(values, labels = labels, colors = colors, explode = explode, autopct='%1.1f%%', shadow = True)
plt.show()