# Example 3.4 
# Program to check validity of a Phone Number using a Function
# Function to check validity of a Phone Number
def checkPhoneNumber(number):
  print (number)
  print (len(number))
  if len(number) != 12:
    return False
  if number[3] != '-':
    return False
  number = number[:3] + number[4:]
  print (number)
  if number[6] != '-':
    return False
  number = number[:6] + number[7:]
  print (number)
  print( number.isdigit())
  return number.isdigit()
# Main Code
phoneNumber = input("Type a Phone Number:")
if checkPhoneNumber(phoneNumber):
  print("valid")
else:
  print("Invalid")