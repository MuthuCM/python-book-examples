# Example 12.7

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

orders_df = pd.read_csv("Summarized_Orders2.csv")
orders_df.head()

# groupby.agg() function

orders_df_results = (orders_df.groupby('Restaurant_Location').
              agg(ORDERS_MEAN = ('number_of_orders', 'mean'),
                  DELIVERY_PERCENTAGE_MEDIAN = ('percentage_of_delivery_orders', 'median')))

orders_df_results.head()

