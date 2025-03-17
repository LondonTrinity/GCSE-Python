#Subprogram1 Challenge 02

def Menu():
    print("1) Domination")
    print("2) Team Deathmatch")
    print("3) Headquarters")

Menu()

playerchoice = int(input("Choose one of the above options (1, 2 or 3) "))

def choosing (choice):
    if choice == 1:
        print("Domination selected")
    elif choice == 2:
        print("Team Deathmatch selected")                        
    elif choice == 3:
        print("Headquarters selected")
    else:
        print("Invalid input")
choosing(playerchoice)

