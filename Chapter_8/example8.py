# Example 8.8
# Program to read an image from a binary file & write it into another binary file
# A File which is opened in binary mode
# will return its contents as bytes without any decoding
with open("dog.jpg","rb") as file_object_8,open("new_dog.jpg","wb")as file_object_8A:
  for each_line_bytes in file_object_8:
    file_object_8A.write(each_line_bytes)