#INPUT EXPLAINED


#Input is a FUNCTION

#It allows a user to input data into
#... a program via the keyboard

#It can also display strings

#Here is a variable:
name = ""

#Here is a variable with an input:
name = input("enter name")

#This will display "enter name"
#The user should then enter a string
#Then press enter
#The data entered will be stored in the variable

#This data can be displayed later
print(name)


#Example:

name = input("What is your name? ")
age = input("What is your age? ")
favColour = input("What is your favourite colour? ")

print("Your name is", name, "and you are" , age, "years old. Your favourite colour is also" , favColour , ".")

if name == "London":
    print("Your name is the same as mine!")
else:
    print("We have different names.")


#CASTING INTRODUCED

#Casting is a WAY TO CHANGE DATA TYPES

#Example:
age = str(input("What is your age? "))
ageInt = int(age)
total = ageInt + 10
print(total)

#The following functions allow you to "CAST"

int()
str()
float()
