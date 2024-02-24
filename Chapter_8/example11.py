#Example 8.11
#Program to write given data to a CSV file
import csv
header_record = ['state','capital']
content_records = [['TamilNadu','Chennai'],['Karnataka','Bengaluru'],['Maharashtra','Mumbai'],['West Bengal','Kolkatha']]
with open('state_capitals.csv','w',newline='') as file_object_11:
  csv_writer = csv.writer(file_object_11)
  csv_writer.writerow(header_record)
  csv_writer.writerows(content_records)