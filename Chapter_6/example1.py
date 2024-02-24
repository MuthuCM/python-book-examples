# Example 6.1
# Creating a Dictionary from user Input
phone_dictionary = {}
for i in range(0,3):
  dictionary_key = input("Type key: ")
  dictionary_value = input("Type value: ")
  phone_dictionary.update({dictionary_key:dictionary_value})
print(f"Dictionary is {phone_dictionary}")