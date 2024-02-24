import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

orders_df = pd.read_csv("Summarized_Orders2.csv")
orders_df.head()



orders_df.number_of_orders.describe()

orders_df.number_of_orders.plot(kind = 'box')

