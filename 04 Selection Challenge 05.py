#Selection challenge 05:

rain = input("Is it raining today? ")
rain = rain.lower()

if rain == "yes":
    windy = input("Is it windy today? ")
    windy = windy.lower()
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")
