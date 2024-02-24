# Example 13.6

import numpy as np
import pandas as pd

left_df = pd.DataFrame({"Ranking":[1,2,3,4,5 ],
                     "Company":['OpenAI','Karya','NVidea','Curai','Encode'],
                 "Founder":['Sam','Manu','Jesan', 'Neal','Sneha']

                     })
left_df.head()

right_df = pd.DataFrame({"Ranking":[1,2,3,4,5 ],
                     "Company":['Shalom','WadhwaniAI','Astrix','Refiberd','Nallas'],
                 "Founder":['Kalika','Sam','Jesan', 'Tushmita','Senthil']

                     })
right_df.head()

# "outer merge" Demo

outer_merged_df = pd.merge(left_df, right_df, left_on = 'Founder', right_on = 'Founder', how = 'outer')

outer_merged_df.head(10)