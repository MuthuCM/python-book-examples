# Example 5.4
# Linear Search
# Program to find position of occurence of a value in a list
values = list(eval(input("Type a list of values: ")))
search_value = int(input("Type the value whose index position is needed: "))
for i in range(0,len(values)):
  if values[i] == search_value:
    print(f"{search_value} occurs at the position {i}")
    break
else:
  print(f"{search_value} does not occur in the given List")