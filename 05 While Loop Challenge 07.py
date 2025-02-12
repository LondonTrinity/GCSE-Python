#05 While Loop Challenge 07

var = 10
guess = 0

while var != 0:
    while guess != var:
        print("There are {} green bottles hanging on the wall,".format(var))
        print("{} green bottles hanging on the wall, ".format(var))
        print("And if one green bottle should accidentally fall")
        var -= 1
        guess = int(input("How many green bottles will be hanging on the wall? "))
    
        if guess == var:
            print("There'll be {} green bottles hanging on the wall.".format(var))
        else:
            print("Try again")
    guess -= 1
print("There'll be no green bottles hanging on the wall.")

    
        
