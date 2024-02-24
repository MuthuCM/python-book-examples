# Example 7.3
# Swapping two values without using an intermediate variable
a = eval(input("Type the First Number: "))
b = eval(input("Type the Second Number: "))
b , a = a , b  # a , b is a Tuple . Unpacking is done here.
print(f"First Number after Swapping is : {a}")
print(f"Second Number after Swapping is : {b}")