# Example 7.2
# Creating a Tuple with user-entered data
tuple1 = ()
no_of_items = int(input("Type the total number of items in Tuple: "))
for i in range(0,no_of_items):
  item = input("Type an item to add in Tuple: ")
  tuple1 = tuple1 + (item,)
print(f"Items in the Tuple are {tuple1}")