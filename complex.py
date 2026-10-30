#Create a complex calculator using inputoutput and control flows.
num1 = float(input("Enter number one: "))
num2 = float(input("Enter number two: "))
operator = input("Enter the operator(+ / * - ** %): ")

if operator == "+":
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}")

elif operator == "-":
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is {result}")

elif operator == "*":
    result = num1 * num2
    print(f"The product of {num1} and {num2} is {result}")

elif operator == "**":
    result = num1 ** num2
    print(f"The power of {num1} to {num2} is {result}")

elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        print(f"The modulus of {num1} and {num2} is {result}")

    else:
        print("Modulus by zero is invalid!")

   
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The division of {num1} and {num2} is {result}")

    else:
        print("Division by zero is invalid!")

else:
    print("Invalid operator!")

     