# Example 12.2
# Bar Chart - Example 1
#import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
flights_df = sns. load_dataset ('flights')
flights_df.head()

yearwise_passenger_count_df = flights_df.groupby('year').passengers.sum().reset_index()
sns.barplot(data = yearwise_passenger_count_df, x = 'year', y = 'passengers')
plt.xlabel('Year')
plt.ylabel('Passengers')
plt.title('Passengers per Year')
plt.show()

