# Example 8.7
# Program to find the longest word in a Text File
with open("file8.txt","r") as file_object_7:
  longest_word = ""
  for each_line in file_object_7:
    each_line = each_line.rstrip() # Removes trailing spaces
    word_list = each_line.split() # splits a line into words
    for each_word in word_list:
      if len(each_word)>len(longest_word):
        longest_word = each_word
  print(f"Longest Word in the File is: {longest_word}")