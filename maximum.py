
#"Write a program that takes three numbers and determines which one is the largest."
num1 = float(input("Enter number one: "))
num2 = float(input("Enter number two: "))
num3 = float(input("Enter number three: "))

if num1 >= num2 and num1 >= num3:
    largest = num1

elif num2 >= num1 and num2 >= num3:
    largest = num2

else:
    largest = num3

print(f"The largest number between {num1}, {num2} and {num3} is {largest}.")