# Example 8.1
# Program to read and display the contents of a File
file_object_1 = open("datascience.txt","r")
for each_line in file_object_1:
  print(each_line)
file_object_1.close()