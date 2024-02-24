# Example 12.1
# groupby() example
#import numpy as np
#import pandas as pd
import seaborn as sns
flights_df = sns. load_dataset ('flights')
flights_df.head()

flights_df.groupby('year').passengers.sum()

flights_df.groupby('month').passengers.sum()

flights_df.groupby('year').passengers.sum().pct_change() * 100

