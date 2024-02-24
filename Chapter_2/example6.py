# Example 2.6
# Program to find the sum of digits in a Number
number = int(input("Type a Number: "))
sum = 0
while number != 0:
  digit = number % 10
  sum = sum + digit
  number = number // 10
print(f"Sum of digits in the given number is {sum}")