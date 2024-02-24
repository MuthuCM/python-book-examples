# Example 7.7
# Program for membership Testing
southern_states = {"TamilNadu","Kerala","Karnataka","Andhra","Telangana"}
state = input("Type the name of the State: ")
if state in southern_states:
  print(f"{state} is a Southern State")
else:
  print(f"{state} is not a Southern State")