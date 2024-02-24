import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
orders_df = pd.read_csv("Summarized_Orders2.csv")
orders_df.head()

(orders_df.Restaurant_Location == 'Vashi').head()

def is_Vashi(Restaurant_Location):
  return Restaurant_Location == 'Vashi'

orders_df.Restaurant_Location.apply(is_Vashi).head()

import time

start_time = time.time()

# Your code here
orders_df.Restaurant_Location.apply(is_Vashi).head()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time} seconds")

import time

start_time = time.time()

# Your code here
(orders_df.Restaurant_Location == 'Vashi').head()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time} seconds")