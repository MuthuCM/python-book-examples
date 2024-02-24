# Example 5.5
# Sorting
# Program to sort a set of values in ascending order
values = list(eval(input("Type a list of values: ")))
for i in range(0,len(values)-1):
  for j in range(i+1, len(values)):
    if values[j] < values[i]:
      temp = values[i]
      values[i] = values[j]
      values[j] = temp

for k in range(0,len(values)):
  print(f"{values[k]}")