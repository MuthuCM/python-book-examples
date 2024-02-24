# Example 2.11
# Program to find whether a Number is a Prime Number
# Program to find whether a given Number is a Prime No.
number = int(input("Type a Number: "))
for i in range(2,number):
  if number % i == 0:
    print(f"{number} is not a Prime Number")
    break
else:
  print(f"{number} is a Prime Number")