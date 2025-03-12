#08 Random Module Challenges 08

import random

score = 0

for i in range (5):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    answer = num1 + num2
    print("Question", i + 1, ":", num1, "+", num2, "= ")
    Their_Answer = int(input())
    if Their_Answer == answer:
        print("Well done")
        score += 1
print("You scored: {}/5".format(score))
