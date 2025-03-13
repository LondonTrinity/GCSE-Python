#1D Array/List1 Challenges 03

names = []
count = True

for i in range (3):
    people = input("Enter the names of people you want to invite to the party: ")
    names.append(people)

while count:
    morePeople = input("Do you want to add more names? ")

    if morePeople == "no":
        count = False

    else:
        people = input("Enter the name of the person you want to invite: ")
        names.append(people)

length = len(names)

print("You have invited {} people to the party.".format(length))
