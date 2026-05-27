from Main_tea import Preferences, TeaRecommender

#function, that is used to receive score
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
print("Tea Recommendation, answer further questions, and you will know your best tea")

sweetness = ask_scale("How sweet?")
sourness = ask_scale("How sour?")
bitterness = ask_scale("How bitter?")
strength = ask_scale("How strong?")
#creating user's prefs as an object
prefs = Preferences(sweetness, sourness, bitterness, strength)
#calling recommend system
system = TeaRecommender()
tea, score = system.recommend(prefs)
#conclusion
print("\nYour best tea is: ", tea)
print(f"Best match: {tea.name}")
print(f"Match score: {score}")
print(f"Brewing: {tea.brew_info()}")