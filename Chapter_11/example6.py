import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
orders_df = pd.read_csv("Summarized_Orders2.csv")
orders_df.head()



orders_df['date_time'] = pd.to_datetime(orders_df['date_time'])
orders_df.date_time.dt.weekday.value_counts().sort_index().plot(kind = 'bar')

orders_df.date_time.dt.weekofyear.value_counts().sort_index().plot(kind = 'bar')

orders_df.date_time.dt.weekofyear.value_counts().sort_index().plot(kind = 'line')

orders_df.number_of_orders.plot(kind = 'hist' , bins = 30)

(orders_df[orders_df.date_time.dt.weekday < 5]
 .number_of_orders
 .plot(kind = 'hist' , bins = 30))

(orders_df[orders_df.date_time.dt.weekday >= 5]
 .number_of_orders
 .plot(kind = 'hist' , bins = 30))

orders_df['date_time'] = pd.to_datetime(orders_df['date_time'])
(orders_df[orders_df.date_time.dt.weekday < 5]
 .number_of_orders
 .plot(kind = 'hist' , bins = 30, density = True))
(orders_df[orders_df.date_time.dt.weekday >= 5]
 .number_of_orders
 .plot(kind = 'hist' , bins = 30, density = True, alpha = 0.5))
plt.legend(["Weekdays" , "Weekends"])

for restaurant in orders_df.Restaurant_Location.unique().tolist():
  print(restaurant)
  df = orders_df[orders_df.Restaurant_Location == restaurant]
  # Plot weekday histogram
  (df[df.date_time.dt.weekday < 5].number_of_orders.plot(kind = 'hist' , bins = 30 , density = True))
  # Plot weekend histogram
  weekend_rows = ( df.date_time.dt.weekday >= 5)
  if weekend_rows.sum() > 0 :
    (df[weekend_rows].number_of_orders.plot(kind = 'hist' , bins = 30 , density = True , alpha = 0.5))
  # Add a legend
  plt.legend(['Weekday' , 'Weekend'])
  # Show the plot at each iteration of the "for" loop
  plt.show()

