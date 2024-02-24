# Example 8.9
# Program to write a string in a binary file & then read it
with open("newfile","wb") as file_object_9:
  file_object_9.write(b'abcdef')
with open("newfile","rb") as file_object_9:
  byte = file_object_9.read(1)
  print("Print each byte in the File")
  while byte:
    print(byte)
    byte = file_object_9.read(1)# Example 8.9
# Program to write a string in a binary file & then read it
with open("newfile","wb") as file_object_9:
  file_object_9.write(b'abcdef')
with open("newfile","rb") as file_object_9:
  byte = file_object_9.read(1)
  print("Print each byte in the File")
  while byte:
    print(byte)
    byte = file_object_9.read(1)