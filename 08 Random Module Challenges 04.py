#08 Random Module Challenges 04

import random

num = random.randint(1, 5)
choice = int(input("Pick a number from 1 to 5: "))

if num == choice:
    print("Well done")
    
elif choice > num:
    choice = int(input("Too high, try again: "))
    if num == choice:
        print("Correct")
    else:
        print("You lose")
    
elif choice < num:
    choice = int(input("Too low, try again: "))
    if num == choice:
        print("Correct")
    else:
        print("You lose")


    
    


        


