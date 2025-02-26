#07 String Slice Challenges 06

firstName = input("Enter your first name: ")

if len(firstName) < 5:
    lastName = input("Enter your last name: ")
    wholeName = firstName + lastName
    print(firstName.upper())
else:
    print(firstName.lower())
