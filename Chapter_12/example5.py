# Example 12.5

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

orders_df = pd.read_csv("Summarized_Orders2.csv")
orders_df.head()

# size() function

orders_df.groupby('Restaurant_Location').size()