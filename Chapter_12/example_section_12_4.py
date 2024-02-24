# Section 12.4
import numpy as np

import pandas as pd
pt_students_info = {"Name":['Andrew','Thomas','Albert','Giftson','Daniel','Benny','Milton','Charles','Benedict' ],
                     "Year":[1,1,1,3,2,2,3,1,1],
                 "State":['TN','TN','KL', 'DL','TN','KL','TN','DL','DL'],
                     "Age" : [18,19,19,22,21,19,20,17,18],
                     "DA_mark" : [98,80,np.nan,60,70,np.nan,np.nan,np.nan,98],
                     "DV_mark" : [80,np.nan,np.nan,40,50,np.nan,np.nan,60,65]
                     }
pt_students_df = pd.DataFrame(pt_students_info)
pt_students_df

pt_students_df.groupby('Year')[['DA_mark','DV_mark']].mean()

results_df = (pt_students_df.groupby('Year').
              agg(MEAN_DA_MARK = ('DA_mark', 'mean'),
                  MEDIAN_DV_MARK = ('DV_mark', 'median')))
results_df

