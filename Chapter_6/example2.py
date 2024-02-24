# Example 6.2
# Traversing a Dictionary
capital_dictionary = {"India":"Delhi","Srilanka":"Colombu","Nepal":"Katmandu"}
for country,capital in capital_dictionary.items():
  print(f"'{country}' has the capital '{capital}'")
# Displaying keys in the Dictionary
for country in capital_dictionary.keys():
  print(country)
# Displaying values in the Dictionary
for capital in capital_dictionary.values():
  print(capital)