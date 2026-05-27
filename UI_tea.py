from Main_tea import Preferences, TeaRecommender

#function for asking values
def ask_scale(question):
    while True:
        val = input(question + " (1-10 or exit): ")
        if val.lower() == "exit":
            exit()
        if val.isdigit():
            val = int(val)
            if 1 <= val <= 10:
                return val
        print("Invalid input")


#dialogue with user
print("Tea Recommendation System")
print("Answer the following questions.\n")

sweetness = ask_scale("How sweet do you want the tea?")
sourness = ask_scale("How sour do you want the tea?")
bitterness = ask_scale("How bitter do you want the tea?")
strength = ask_scale("How strong do you want the tea?")

#creating preferences object
prefs = Preferences(sweetness, sourness, bitterness, strength)

#recommendation system
system = TeaRecommender()
tea, score, sugar, lemon = system.recommend(prefs)

# conclusion
print("\nResults:")
print("Sugar: no sugar")
print(f"Best tea: {tea.name}")
print(f"Match score: {score} out of 40")
print(f"Brewing: {tea.brew_info()}")

#sugar
if sugar == 0:
    print("Sugar: no sugar")
elif sugar == 1:
    print("Sugar: 1 spoon")
else:
    print(f"Sugar: {sugar} spoons")

#lemon
if lemon == 0:
    print("Lemon: no lemon")
elif lemon == 1:
    print("Lemon: 1 slice")
else:
    print(f"Lemon: {lemon} slices")