#08 Random Module Challenges 07

import random

num = random.randint(1, 6)

correct = False

while correct == False:
    guess = int(input("Guess the number: "))
    if guess == num:
        correct = True
    elif guess > num:
        print("Too high")
    else:
        print("Too low")
print("Well done!")
