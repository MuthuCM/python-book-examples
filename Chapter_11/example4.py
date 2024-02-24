# Example 11.4
# Bar Chart
import pandas as pd
new_students_info = {"Name":['Thomas','Andrew','Daniel','Benny','Milton','Giftson' ],
                     "Year":[1,1,2,2,3,3],
                 "State":['TN','TN','KL', 'KL','AP','TN'],
                     "Age" : [19,18,20,19,20,21],
                     "DA_mark" : [80,92,70,85,83,84],
                     "DV_mark" : [82,95,74,85,86,88]
                     }
new_students_df = pd.DataFrame(new_students_info)
new_students_df

import matplotlib.pyplot as plt
new_students_df.DA_mark.plot(kind = 'bar')

new_students_df.index = new_students_df.Name
new_students_df.DA_mark.plot(kind = 'bar')
new_students_df = new_students_df.reset_index(drop = True)

new_students_df.plot(x = 'Name', y = 'DA_mark', kind = 'bar')

