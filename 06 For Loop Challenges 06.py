#06 For Loop Challenges 06

total = 0

for i in range (5):
    num = int(input("Enter a number: "))
    add = input("Do you want to include that number? y/n ")
    if add == "y":
        total += num

print(total)
