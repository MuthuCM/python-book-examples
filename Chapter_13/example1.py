# Example 13.1
# concat() function Demo
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

concatenated_df = pd.concat([left_df,right_df])

concatenated_df .head(10)

