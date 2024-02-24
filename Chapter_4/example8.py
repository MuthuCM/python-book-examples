# Program to draw Pie Chart 
# Import Libraries
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
# Specify Data
labels = ["Raw Materials","Labour","Rent","Electricity"]
values = [30,90,30,30]
palette_color = sns.color_palette('bright')
explode = [0, 0.1, 0, 0]
colors = ['b','g','r','c']
# Draw a Pie Chart
#plt.pie(values, labels = labels, colors = colors, explode = explode, autopct='%1.1f%%', shadow = True)
plt.pie(values, labels=labels, colors=palette_color, autopct='%.0f%%')
plt.show()