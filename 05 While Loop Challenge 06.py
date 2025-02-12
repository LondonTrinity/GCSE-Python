#05 While Loop Challenges 06

num = int(input("Enter a number between 10 and 20: "))

while num < 10 or num > 20:
    if num < 10:
        print("Too low")
        num = int(input("Try again: "))
    elif num > 10:
        print("Too high")
        num = int(input("Try again: "))

print("Thank you")
