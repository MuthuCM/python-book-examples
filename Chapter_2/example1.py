# Example 2.1
# Profession Tax calculation
salary = int(input(" Type Your Salary: "))
if salary >= 45000:
  profession_tax = 0.10 * salary
  print(f"Profession Tax = Rs. {profession_tax:8.2f}")