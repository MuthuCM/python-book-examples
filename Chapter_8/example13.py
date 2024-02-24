#Example 8.13
#Program to write data to a CSV file using DictWriter class
import csv
with open('pincodes.csv','w', newline='') as file_object_13:
  column_names = ['capital','pincode']
  writer = csv.DictWriter(file_object_13, fieldnames = column_names)
  writer.writeheader()
  writer.writerow({'capital':'Chennai','pincode':'600001'})
  writer.writerow({'capital':'Bengaluru','pincode':'500001'})
  writer.writerow({'capital':'Mumbai','pincode':'400001'})
  writer.writerow({'capital':'Kolkatha','pincode':'800001'})