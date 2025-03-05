#08 Random Module Challenges 06

import random

num = random.randint(1, 10)
correct = False

while correct == False:
    guess = int(input("Guess a number: "))
    
    if guess == num:
        correct = True
    elif guess > num:
        print("Too high")
    else:
        print("Too low")

print("You are correct")
        

