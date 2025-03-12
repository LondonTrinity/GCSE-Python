#08 Random Module Challenges 08

import random

colours = ["red", "orange", "yellow", "blue", "green"]

print("The list is:", colours)

computer = random.choice(colours)
guess = " "

while guess != computer:
    guess = input("Pick a random colour from the list: ")
    if guess == computer:
        print("Well done")
    else:
        if computer == "red":
            print("I could really do with some RED paint...")
        elif computer == "orange":
            print("I am really hungry, do you have an ORANGE by any chance???")
        elif computer == "yellow":
            print("Wow, the sun looks really YELLOW today!!!")
        elif computer == "blue":
            print("You are probably feeling BLUE right now because you guessed wrong...")
        else:
            print("I bet you are GREEN with envy...")

