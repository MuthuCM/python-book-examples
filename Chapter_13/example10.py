# Example 13.10

import numpy as np
import pandas as pd

weather_df = pd.read_csv("weather1.csv")
weather_df.DATETIME = pd.to_datetime(weather_df.DATETIME)
weather_df.head()

num_orders_df = pd.read_csv("num_orders1.csv")
num_orders_df.DATETIME = pd.to_datetime(num_orders_df.DATETIME)
num_orders_df.head(5)

merged_df1 = pd.merge(num_orders_df , weather_df , on = 'DATETIME' , how = 'left')
merged_df1.head(15)

merged_df1.plot( x = 'TEMPERATURE' , y = 'NUM_ORDERS' , kind = 'scatter')

((merged_df1.TEMPERATURE/10).round() * 10).head()

merged_df1.groupby((merged_df1.TEMPERATURE/10).round() * 10).NUM_ORDERS.sum().plot(kind = 'bar')

