# Example 5.10
# Program to find common elements of two Lists using List Comprehension
x = [11,11,12,13,15,18,23,31,44,65,99]
y = [11,12,13,14,15,16,17,18,19,20,21,22,23]
result = [x[i] for i in range(len(x)) if x[i] in y and x[i] not in x[:i]]
print(result)