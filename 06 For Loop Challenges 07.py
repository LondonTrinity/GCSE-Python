#06 For Loop Challenges 07

direction = input("Do you want to count up or down? u/d ")

if direction == "u":
    top = int(input("Enter the top number: "))
    for i in range (1, top + 1):
        print(i)
elif direction == "d":
    low = int(input("Enter a number below 20: "))
    for i in range (20, low - 1, -1):
        print(i)
