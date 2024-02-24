# Example 8.3
# Program to read from a File using read() method
with open("datascience.txt","r") as file_object_3:
  #file_content = file_object_3.read()   # Command to read entire content
  file_content = file_object_3.read(50)
  print(file_content)