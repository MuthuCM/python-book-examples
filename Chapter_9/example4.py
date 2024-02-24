# Example 9.4
# Defining Abstraction - implementation Hiding
class Quadrant:
  def __init__(self,x,y):
    self.x_coordinate = x
    self.y_coordinate = y
  def find_quadrant(self):
    if self.x_coordinate > 0 and self.y_coordinate > 0 :
      print(f"Point({self.x_coordinate} , {self.y_coordinate}) lies in First Quadrant")
    elif self.x_coordinate < 0 and self.y_coordinate < 0 :
      print(f"Point({self.x_coordinate} , {self.y_coordinate}) lies in Third Quadrant")
    elif self.x_coordinate > 0 and self.y_coordinate < 0 :
      print(f"Point({self.x_coordinate} , {self.y_coordinate}) lies in Fourth Quadrant")
    elif self.x_coordinate < 0 and self.y_coordinate > 0 :
      print(f"Point({self.x_coordinate} , {self.y_coordinate}) lies in Second Quadrant")
# Object Creation
point = Quadrant(40,20)
point.find_quadrant()