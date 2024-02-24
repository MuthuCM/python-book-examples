# Example 6.7
# Storing Month Numbers & Month Names in a Dictionary
# Function Definition
def prettyDate(date):
  months = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
  month = months[int(date[0:2])]
  day = date[2:4]
  year = date[4:8]
  formatted_date = month + " " + day + "," + year
  print (formatted_date)
# Main Code
date = input("Type Date in MMDDYYYY format: ")
prettyDate(date)