# Example 13.3

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

# "inner merge" & "outermerge" Demo
inner_merged_df = pd.merge(left_df, right_df, left_on = 'Founder', right_on = 'Founder', how = 'inner')
inner_merged_df.head(10)

inner_merged_df = pd.merge(left_df, right_df, left_on = 'Founder', right_on = 'Founder')
inner_merged_df.head(10)

inner_merged_df = pd.merge(left_df, right_df, on = 'Founder', how = 'inner')
inner_merged_df.head(10)