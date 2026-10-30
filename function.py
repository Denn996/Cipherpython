def greet():
    print("This is my first function")

greet()

#function wit parameters
def student(name,age,course):
    print(f"Student name is {name}")
    print(f"Student age is {age}")
    print(f"Student course is {course}")

student("Dennis",21,"Network Engineering")

#function with return keyword
def add_number(a,b):
    return a + b
result = add_number(6,7)
print(f"Sum : {result}")

def product(k,l):
    return k * l
result = product(10,30)
print(f"Product is : {result}")