# Example 6.4
# Finding no. of times each word appears in a sentence
count_words = dict()
sentence = input("Type a Sentence:")
words = sentence.split()
for each_word in words:
  count_words[each_word]=count_words.get(each_word,0)+1
print(count_words)