# Example 13.8
import numpy as np

import pandas as pd
first_df = pd.DataFrame({"Ranking":[1,2,3,4,5 ],
                     "University":['Madras','Madurai','Bharathiar','Bharathidasan','Thiruvalluvar'],
                 "Professor":['Andrew','Albert','Thomas', 'Giftson','Milton']

                     })
first_df.head()

import numpy as np

import pandas as pd
second_df = pd.DataFrame({"Ranking":[1,2,3,4,5 ],
                     "University":['Cochin','Trivandrum','Calicut','Trichur','Kottayam'],
                 "Professor":['Andrew','Charles','Benedict', 'Thomas','Louie']

                     })
second_df.head()

left_merged_table = pd.merge(first_df, second_df, left_on = 'Professor', right_on = 'Professor', how = 'left')

left_merged_table.head()

