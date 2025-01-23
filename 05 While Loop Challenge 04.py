#05 While Loop Challenge 04

sentry = "y"

count = 0

while sentry == "y":
    name = input("Who do you want to be invited to the party? ")
    print(name, "has now been invited")
    count += 1
    sentry = input("Do you want to add anyone else? Y/N ")

print(count)
    
