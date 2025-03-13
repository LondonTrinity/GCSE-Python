#1D Arrary/List1 Challenges 02

cars = []

count = True

while count:
    choice = input("Input a car brand or press x to exit: ")

    if choice == "x":
        print("exiting...")
        count = False
    else:
        cars.append(choice)

print("In the list is: ", cars)
