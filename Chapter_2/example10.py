# Example 2.10
# Program to find factorial of a number
number = int(input("Type a Number: "))
factorial = 1
for i in range(1 , number+1):
  factorial = factorial * i
print(f"Factorial of {number} = {factorial} ")