#05 While Loop Challenge 03

num = int(input("Enter a number: "))

num1 = num

total = num1

y = "y"

while y == "y":
    num2 = int(input("Enter a number: "))
    total = num1 + num2
    y = input("Do you want to add another number? Y/N ")
    y = y.lower()

print(total)
        
