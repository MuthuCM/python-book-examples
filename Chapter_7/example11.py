# Example 7.11
# Finding Unique Words in a Sentence.Duplicate words will be removed.
sentence = "The wise girl solved the puzzle quickly"
sentence = sentence.lower()
words = sentence.split()
print(f"Unique Words are: {list(set(words))}")
print(f"Unique Sorted Words are: {sorted(list(set(words)))}")