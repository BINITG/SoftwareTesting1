class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person("Binit",30)
p2=person("sony",28)

print(p1.name)
print(p1.age)


#create a class ang get values using method in class.

class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}\nRoll Number: {self.roll_number}\nGrade: {self.grade}"

# Creating an instance of the Student class
student1 = Student("John Doe", "S12345", "A")

# Calling the get_details method to get the student details
details = student1.get_details()

# Printing the details
print(details)
