from Main_tea import Conclusion, BrewTea, Factory #importing classes from main

#asking user to create his own tea

allowed_tea_types = ["black", "green", "red"]

#tea type
while True:
    tea_type = input("Input tea type (or 'exit' to exit): ").lower()
    if tea_type == "exit":
        exit()

    if tea_type in allowed_tea_types:
        break
    else:
        print("wrong input")

#temperature
while True:
    temp = input("Input temperature of water (or 'exit' to exit): ")
    if temp.lower() == "exit":
        exit()
    if temp.isdigit() or (temp.startswith("-") and temp[1:].isdigit()):
        temp = int(temp)
        if 0 <= temp <= 100:
            break
    print("wrong input")

#brewing time
while True:
    brew_time = input("Input duration of brewing (or 'exit' to exit): ")
    if brew_time.lower() == "exit":
        exit()
    if brew_time.isdigit() and int(brew_time) >= 0:
        brew_time = int(brew_time)
        break
    print("wrong input")

#sugar
while True:
    sugar = input("Input amount of sugar (or 'exit' to exit): ")
    if sugar.lower() == "exit":
        exit()
    if sugar.isdigit() and int(sugar) >= 0:
        sugar = int(sugar)
        break
    print("wrong input")

#lemon
while True:
    islemon = input("Do you want lemon (yes/no or 'exit' to exit): ").lower()
    if islemon == "exit":
        exit()
    if islemon == "yes":
        lemon = True
        break
    elif islemon == "no":
        lemon = False
        break
    print("wrong input")

#milk ratio
while True:
    milk_ratio = input("Input milk ratio (0-1 or 'exit'  to exit): ")
    if milk_ratio.lower() == "exit":
        exit()
    try:
        milk_ratio = float(milk_ratio)
        if 0 <= milk_ratio <= 1:
            break
    except ValueError:
        pass
    print("wrong input")

#creating object tea and outputing data about it

tea = Factory.create_tea(tea_type)
tea.describe()

#brewing the tea and checking what is inside

brewedtea = BrewTea(tea, temp, brew_time, sugar, lemon, milk_ratio)
print("Your tea:")
brewedtea.describe()

Conclusion.score(brewedtea)
Conclusion.description(brewedtea)