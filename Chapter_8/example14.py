#Example 8.14
#Program to read data from a CSV file using DictReader class
import csv
with open('pincodes.csv','r', newline='') as file_object_14:
  reader = csv.DictReader(file_object_14)
  for each_record in reader:
    print(f"{each_record['capital']},{each_record['pincode']}")