# Example 6.5
# Calculating no. of digits, uppercase & lowercase letters in a string
sentence = input("Type a Sentence: ")
count_dictionary={"digit":0,"lowercase":0,"uppercase":0}
for each_character in sentence:
  if each_character.isdigit():
    count_dictionary["digit"]=count_dictionary["digit"]+1
  elif each_character.isupper():
    count_dictionary["uppercase"]=count_dictionary["uppercase"]+1
  elif each_character.islower():
    count_dictionary["lowercase"]=count_dictionary["lowercase"]+1
print(count_dictionary)