# Example 4.11
# Hexagonal Binning Plot
# Hexagonal Binning Plot ia a fancier version of Scatter Plot
# Import Libraries
#%matplotlib inline
import seaborn as sns
# Specify Data
mpg_df = sns.load_dataset("mpg")
# set the plot style to include ticks on the axes.
sns.set(style="ticks")
# Hexbin plot
sns.jointplot(x = "weight", y= "mpg", data = mpg_df, kind="hex", color="#4CB391")