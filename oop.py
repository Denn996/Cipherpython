class Student:
    #constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age

#object
student1 = Student("Dennis",21)

print(f"Student name: {student1.name}")