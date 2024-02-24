# Example 4.13
# Bar Plot - Diamonds Dataset
# Import Libraries
import matplotlib.pyplot as plt
import seaborn as sns
# Specify Data
diamonds_df = sns.load_dataset('diamonds')
# Draw Bar Chart
sns.barplot(x = "cut", y = "price" , hue = 'color', data=diamonds_df)