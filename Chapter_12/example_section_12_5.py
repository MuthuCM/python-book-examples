# Section 12.5
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
orders_df = pd.read_csv("Summarized_Orders2.csv")
orders_df.head()

orders_df['date_time'] = pd.to_datetime(orders_df['date_time'])
orders_df.set_index('date_time').resample('w').number_of_orders.mean().reset_index().head()

orders_df.set_index('date_time').resample('m').number_of_orders.sum().reset_index().head()

orders_df.set_index('date_time').resample('m').number_of_orders.sum().sort_values().plot(kind = 'bar')

orders_df.set_index('date_time').resample('d').size().rolling(14).mean().plot()

