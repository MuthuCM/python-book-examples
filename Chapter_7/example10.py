# Example 7.10
# Finding unique characters in each one of the given collection of words
def find_unique_characters(*words):
  for each_word in words:
    character_set = sorted(list(set(each_word)))
    print(f"Unique Characters in the word {each_word} are: {character_set}")
# Main Code
find_unique_characters("good","better","best")