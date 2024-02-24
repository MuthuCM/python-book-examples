# Example 4.8
# Category Plot using Seaborn
# Import Libraries
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
# Specify Data
mpg_df = sns.load_dataset("mpg")
# Create Category Plot
#sns.catplot(x = 'origin' , y = 'weight' , kind = 'violin' , data = mpg_df)
#sns.catplot(x = 'origin' , y = 'weight' , kind = 'bar' , data = mpg_df)
sns.catplot(x = 'origin' , y = 'weight' , kind = 'box' , data = mpg_df, color = 'r')
