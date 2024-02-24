# Example 9.1
# Defining a class named "Rectangle"
class Rectangle:
      def __init__ (self, length, breadth):
        self.length = length
        self.breadth = breadth
      def calculate_area (self) :
        area = self.length * self.breadth
        return area
      def calculate_perimeter (self) :
        perimeter = 2 *(self.length + self.breadth)
        return perimeter
# Main Code
length = int(input("Type Length of Wall: "))
breadth = int(input("Type Bredth of Wall: "))
wall = Rectangle (length, breadth)
wall_area = wall.calculate_area( )
wall_perimeter = wall.calculate_perimeter( )
print(f"Area of Wall = {wall_area} square feet")
print(f"Perimeter of Wall = {wall_perimeter} feet")