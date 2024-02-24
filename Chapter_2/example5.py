# Example 2.5
# Program for Bonus Calculation
category = input("Type the category of Employee(Executive/Technician): ")
salary = int(input("Type the Salary of Employee: "))
if category == "Executive":
  if salary > 100000:
    bonus = 0.30 * salary
  else:
    bonus = 0.20 * salary
else:
  bonus = 0.10 * salary

print(f"Category:{category} ")
print(f"Salary  :{salary} ")
print(f"Bonus   :{bonus : 8.2f} ")