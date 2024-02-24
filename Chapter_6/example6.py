# Example 6.6
# Storing Reg No & Mark for each Student in a Dictionary
student_details ={}
for i in range(0,5):
  name = input("Type Student Name: ")
  register_number = input("Type Register Number: ")
  mark = input("Type Mark: ")
  student_details[name]=[register_number,mark]
student_name = input("Type Student Name whose details are needed: ")
if student_name not in student_details.keys():
  print(f"{student_name} is not present in the List")
else:
  print(f"Register Number is: {student_details[student_name][0]}")
  print(f"Mark is: {student_details[student_name][1]}")