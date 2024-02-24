# Example 12.4
# Bar Chart - Example 3
# Summarized_Orders dataset from Mattan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
orders_df = pd.read_csv("Summarized_Orders2.csv")
orders_df.head()

orders_df.groupby('Restaurant_Location').number_of_orders.mean()

orders_df.groupby('Restaurant_Location').number_of_orders.mean().reset_index()

orders_df.groupby('Restaurant_Location').number_of_orders.mean().plot(kind = 'bar')

