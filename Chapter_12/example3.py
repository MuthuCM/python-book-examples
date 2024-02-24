# Example 12.3
# Bar Chart - Example 2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
flights_df = sns. load_dataset ('flights')
flights_df.head()

monthwise_passenger_count_df = flights_df.groupby('month').passengers.sum().reset_index()
sns.barplot(data = monthwise_passenger_count_df, x = 'month', y = 'passengers')
plt.xlabel('Month')
plt.ylabel('Passengers')
plt.title('Passengers per Month')
plt.show()

