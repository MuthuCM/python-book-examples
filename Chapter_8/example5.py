# Example 8.5
# Program to reverse each word in a Text File
reversed_word_list = []
with open("file7.txt","r") as file_object_5:
  for each_line in file_object_5:
    #each_line = each_line.rstrip() # Removes trailing spaces
    word_list = each_line.split() # splits a line into words
    for each_word in word_list:
      reversed_word_list.append(each_word[::-1]) # Reverse a Word
      reversed_word_list.append(" ")
    reversed_word_list.append("\n")
  print("".join(reversed_word_list))