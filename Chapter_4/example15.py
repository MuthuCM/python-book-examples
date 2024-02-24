# Example 4.15
# Bar Plot with labels in bigger Font Size - Diamonds Dataset
# Import Libraries
import matplotlib.pyplot as plt
import seaborn as sns
# Specify Data
diamonds_df = sns.load_dataset('diamonds')
# Draw Bar Chart
ax = sns.barplot(x = "cut", y = "price" , hue = 'color', data=diamonds_df)
# Define Legend
ax.legend(loc = 'upper right' , ncol = 4)
# Define Font Size
ax.set_xlabel('cut' , fontdict = {'fontsize' : 15})
ax.set_ylabel('price' , fontdict = {'fontsize' : 15})