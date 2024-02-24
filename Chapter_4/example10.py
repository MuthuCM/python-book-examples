# Example 4.10
# Scatter Plot using Seaborn
# Import Libraries
#%matplotlib inline
import seaborn as sns
# Specify Data
mpg_df = sns.load_dataset("mpg")
# Create Scatter Plot
sns.scatterplot(x = 'weight' , y = 'mpg' , data = mpg_df, color = 'g')