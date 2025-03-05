#08 Random Module Challenges 05

import random

num = random.randint(1, 10)
correct = False

while correct == False:
    guess = int(input("Guess a number: "))
    
    if guess == num:
        correct = True

print("You are correct")
        

