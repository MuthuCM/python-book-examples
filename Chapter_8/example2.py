# Example 8.2
# Program to read and print each Line in a File using "with" st
with open("datascience.txt","r") as file_object_2:
  for each_line in file_object_2:
    print(each_line)