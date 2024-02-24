# Example 11.3
# value_counts() example 2
import seaborn as sns
diamonds_df = sns. load_dataset ('diamonds')
diamonds_df.head()

diamonds_df.color.value_counts()

diamonds_df.color.value_counts(normalize = True)

diamonds_df.color.value_counts(normalize = True).reset_index()

diamonds_df.clarity.value_counts()

diamonds_df.cut.value_counts()