# Example 5.8
# Program to carry out Queue Operations
import collections
queue = collections.deque(["Andrew","Thomas","Albert","Louie"])
print(f"Initial Items are {queue}")
queue.append("Benny")
queue.append("Gerald")
print(f"Items after addition are {queue}")
print(f"Removed item from Queue is {queue.popleft()}")
print(f"Removed item from Queue is {queue.popleft()}")
print(f"Items after removal are {queue}")