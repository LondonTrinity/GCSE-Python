#06 For Loop Challenges 08

user = int(input("How many people do you want to invite to a party? "))

if user < 10:
    for i in range (1, user + 1):
        name = input("Enter the name: ")
        print(name, "has been invited")
elif user >= 10:
    print("Too many people")
