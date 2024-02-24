# Example 2.4
# Program to find the elder person
age1 = int(input("Type First Person's Age: "))
age2 = int(input("Type Second Person's Age: "))
if age1 > age2:
  print("First Person is the Elder")
elif age2 > age1:
  print("Second Person is the Elder")
else:
  print("Both Persons are of same age")