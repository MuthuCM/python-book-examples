# Example 11.1
# describe() example
import seaborn as sns
flights_df = sns. load_dataset ('flights')
flights_df.head()

flights_df.passengers.describe()
