# Example 5.1
# Creating a List from User Input
item_list = []
no_of_items = eval(input("Type total number of items in List:"))
for i in range(0,no_of_items):
  item = input("Type an item to add: ")
  item_list.append(item)
print(f"Items in the List are {item_list}")