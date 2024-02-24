# Example 7.1
# Creating a Tuple(Remember: Tuple is immutable)
register_numbers = ("24PDS001","24PDS002","24PDS003","24PDS004","24PDS005")
#register_numbers = "24PDS001","24PDS002","24PDS003","24PDS004","24PDS005"
#list1 = ["24PDS001","24PDS002","24PDS003","24PDS004","24PDS005"]
#register_numbers = tuple(list1)
# Traversing a Tuple
for each_register_number in register_numbers:
  print(each_register_number)
#register_numbers[0]= "23PDS006" # error will be reported