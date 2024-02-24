# Example 4.16
# Bar Plot with Rotating Labels - Diamonds Dataset
# Import Libraries
import matplotlib.pyplot as plt
import seaborn as sns
# Specify Data
diamonds_df = sns.load_dataset('diamonds')
# Draw Bar Chart
ax = sns.barplot(x = "cut", y = "price" , hue = 'color', data=diamonds_df)
# Define Legend
ax.legend(loc = 'upper right' , ncol = 4)
# Define x-ticks
ax.set_xticklabels(ax.get_xticklabels(), fontsize = 13, rotation = 30)