class Student:
    
    name = "Jaimin"
    yob = 2004
    Gender = "Male"
    
    def find(self):
        print(2024-self.yob)
    
    
    
a1 = Student()
# print(a1.name)
# print(a1.yob)
# print(a1.Gender)
print("Age of ",a1.name,a1.find())
a1.find()

# print("This is Object Value ",a1)
# print("This is Type of Object ",type(a1))
# print("Print the class ",type(Student))