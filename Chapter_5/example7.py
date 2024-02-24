# Example 5.7
# Program to carry out Stack Operations
stack = []
stack_size = 4
def push(item):
  if len(stack) < stack_size:
    stack.append(item)
    print(f"Item added: {item}")
  else:
    print("stack is full")
def pop():
  if len(stack) > 0:
    print(f"item removed: {stack.pop()}")
  else:
    print("stack is empty")
def display():
  print("Items in Stack are:")
  for item in stack:
    print(item)
# Main Code
push(11)
push(12)
push(13)
push(14)
pop()
pop()
display()