# Example 9.7
# Method Overriding
# Defining a class named "Person"
class Person:
      def __init__ (self, name, age):
        self.name = name
        self.age = age

      def get_details(self):
        return self.name, self.age
# Defining a derived class named "Student"
class Student (Person):
      def __init__(self, name,age,rollNumber,mark):
        super (Student, self). __init__ (name, age)
        self.rollNumber = rollNumber
        self.mark = mark

      def get_details(self):
        return self.rollNumber, self.mark
# Main Code
student = Student("Jesudoss", 20 , "24PDS001" , 92)

rollNumber , mark = student.get_details()
print(f"Roll Number  is: {rollNumber}")
print(f"Student Mark is: {mark}")