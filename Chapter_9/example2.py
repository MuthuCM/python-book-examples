# Example 9.2
# Defining a class named "Room"
class Room:
      def __init__ (self, length, breadth,height):
        self.length = length
        self.breadth = breadth
        self.height = height

      def white_washing_area(self):
        wall_area = 2*(self.length*self.height)+2*(self.breadth*self.height)
        ceiling_area = self.length*self.breadth
        total_area = wall_area + ceiling_area
        return total_area

      def white_washing_cost(self):
        cost = self.white_washing_area() * 25
        return cost

# Main Code
length = int(input("Type Length of Class Room: "))
breadth = int(input("Type Bredth of Class Room: "))
height = int(input("Type Height of Class Room: "))
classRoom = Room (length, breadth,height)
whitwashing_cost = classRoom.white_washing_cost()
print(f"Whitewashing Cost = Rs. {whitwashing_cost} ")