# Example 9.6
# Defining a class named "Employee"

class Employee:
      def __init__ (self, name, id):
        self.name = name
        self.id = id
      def getName (self):
        return self.name
      def getId (self):
        return self.id

# Defining a class named "FacultyMember"
class FacultyMember (Employee):
      def __init__(self, name,id,department,designation):
        super (FacultyMember, self). __init__ (name, id)
        self.department = department
        self.designation = designation
      def getDepartment(self):
        return self.department
      def getDesignation (self):
        return self.designation

# Main Code
facultyMember = FacultyMember ("JesuRaj", "DSC002","DataScience" , "Professor")
print(facultyMember.getName())
print(facultyMember.getId())
print(facultyMember.getDepartment())
print(facultyMember.getDesignation())