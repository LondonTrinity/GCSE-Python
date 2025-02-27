#Creating a Calculator with Subprograms

def add (num1, num2):
    total = num1 + num2
    print(total)

def subtract (num1, num2):
    total = num1 - num2
    print(total)

def multiply (num1, num2):
    total = num1 * num2
    print(total)

def divide (num1, num2):
    total = num1 / num2
    print(total)

def choosing_Operator (operator):
    if operator == "add":
        add(n1, n2)
    elif operator == "subtract":
        subtract(n1, n2)
    elif operator == "multiply":
        multiply(n1, n2)
    elif operator == "divide":
        divide(n1, n2)
    else:
        print("This is an invalid operation")

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

function = input("Would you like to add, divide, multiply or subtract? ")
choosing_Operator(function)

