#08 Random Module Challenges 03

import random

coinFlip = ["H", "T"]

coin = random.choice(coinFlip)

guess = input("Guess weather the coin flip is heads (H) or tails (T): ")

if guess == coin:
    print("You win")
elif (guess == "H" and coin == "T") or (guess == "T" and coin == "H"):
    print("It was {}".format(coin))
else:
    print("Bad luck")
