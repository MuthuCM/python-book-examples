# Example 2.7
# Program to find the Lucky Number
number = int(input("Type the digits in Date of Birth: "))
while number > 9:
  sum = 0
  while number != 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10
  number = sum

print(f"Lucky Number is {number}")