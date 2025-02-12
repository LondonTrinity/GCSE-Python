#05 While Loop Challenge 05:

compnum = 50

num = int(input("Enter a number: "))

count = 1

while num != compnum:
    if num > compnum:
        print("Too high")
    elif num < compnum:
        print("Too low")
    num = int(input("Have another guess: "))
    count += 1

if num == compnum:
    print("Well done, you took {} attempts".format(count))
