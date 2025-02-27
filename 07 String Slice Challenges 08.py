#07 String Slice Challenge 08

loops = 1

while loops != 0:
    last_Name = input("Enter your last name: ")
    number = str(loops)
    membership_Number = last_Name[0:3] + number
    print(membership_Number)
    loops += 1
    loops = int(input("Do you want to add another member? Press 0 if not "))
    
    
