#07 String Slice Challenges 07

firstName = input("Enter your first name: ")
vowels = ["a", "e", "i", "o", "u"]
space = " "
length = len(firstName)

for vowel in vowels:
    if firstName[0] == vowel:
        print(space + firstName[1:length])
        
    

