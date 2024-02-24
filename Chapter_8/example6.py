# Example 8.6
# Program to find word frequencies
word_frequencies = dict()
with open("file8.txt","r") as file_object_6:
  for each_line in file_object_6:
    #each_line = each_line.rstrip() # Removes trailing spaces
    word_list = each_line.split() # splits a line into words
    for each_word in word_list:
      word_frequencies[each_word]=word_frequencies.get(each_word,0)+1
  print("The number of times each word appears is:")
  print(word_frequencies)