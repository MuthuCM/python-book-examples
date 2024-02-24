# Example 8.10
# Program to read records from a CSV File 7 display one's details
import csv
with open("biodata.csv",'r',newline='') as file_object_10B:
  csv_reader = csv.reader (file_object_10B)
  name = input("Type name of Person whose details are needed:")
  print(f"Display {name}'s Details")
  for each_record in csv_reader:
    if each_record[0] == name:
      print(",".join(each_record))