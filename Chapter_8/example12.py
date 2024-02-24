#Example 8.12
#Program to read data from state_details.csv & form a Dictionary
import csv
with open('state_capitals.csv','r', newline='') as file_object_12:
  csv_reader = csv.reader (file_object_12)
  next(csv_reader, None)  # skip the header
  print("Display each Record(Row) in CSV File")
  for each_record in csv_reader:
    print(",".join(each_record))