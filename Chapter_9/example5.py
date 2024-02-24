# Example 9.5
# Defining a class named "Person"
class Person:
      def __init__ (self, name, age):
        self.name = name
        self.age = age
      def getName (self):
        return self.name
      def getAge (self):
        return self.age
# Defining a derived class named "Student"
class Student (Person):
      def __init__(self, name,age,rollNumber,mark):
        super (Student, self). __init__ (name, age)
        self.rollNumber = rollNumber
        self.mark = mark
      def getRollNumber(self):
        return self.rollNumber
      def getMark (self):
        return self.mark
# Main Code
student = Student("Mahesh", 20, "24PDS002", 83)
print(student.getName( ))
print(student.getAge( ))
print(student.getRollNumber( ))
print(student.getMark( ))