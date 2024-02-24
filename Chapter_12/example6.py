# Example 12.6
# groupby.aggregate() function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tips_df = sns. load_dataset ('tips')
tips_df.head()

tips_df.groupby('day').sum()

tips_df.groupby('time').sum()

tips_df.groupby('day').total_bill.mean()