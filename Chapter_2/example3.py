# Example 2.3
# Program to calculate Median
values = list(eval(input(" Type the Marks: ")))
values = sorted(values)
size = len (values)

if size % 2 == 1:
	mid = size // 2
	median = values [mid]
	print (f"Median Mark = {median}")
else:
	mid = size // 2
	mid1 = mid -1
	median = (values [mid]+ values[mid1])/2
	print (f"Median Mark = {median}")