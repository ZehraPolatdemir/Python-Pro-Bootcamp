print("Welcome to the Band Name Generator.")
print("----------------------------------------")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
color = input("What is your favorite color?\n")

city = city.capitalize()
pet = pet.capitalize()
color = color.capitalize()

print("\n---Here are your Band Name options.---")
print("Option 1: " + city + " " + pet)
print("Option 2: The " + color + " " + pet + "s")
print("Option 3: " + city + " " + color + " Machine")
