from abc import ABC, abstractmethod

#asking about user's preferences

class Preferences:
    def __init__(self, sweetness, sourness, bitterness, strength):
        self.sweetness = sweetness
        self.sourness = sourness
        self.bitterness = bitterness
        self.strength = strength


#main abstract class tea

class Tea(ABC):
    def __init__(self, name, brew_temp, brew_time):
        self.name = name
        self.brew_temp = brew_temp
        self.brew_time = brew_time

    @abstractmethod
    def match(self, prefs: Preferences) -> float:
        pass
#method, same as describe, used to know how to brew tea correctly
    def brew_info(self):
        return f"{self.brew_temp}°C, {self.brew_time} min"


#classes with types of tea

class BlackTea(Tea):
    def __init__(self):
        super().__init__("Black Tea", 95, 4)
#matching method, that allows user to know score of his tea
    def match(self, prefs):
        score = 0
        score += 10 - abs(prefs.strength - 9)
        score += 10 - abs(prefs.bitterness - 7)
        score += 10 - abs(prefs.sweetness - 3)
        return score

#pretty much the same as black tea, but logic differs
class GreenTea(Tea):
    def __init__(self):
        super().__init__("Green Tea", 80, 3)

    def match(self, prefs):
        score = 0
        score += 10 - abs(prefs.bitterness - 5)
        score += 10 - abs(prefs.sourness - 4)
        score += 10 - abs(prefs.strength - 4)
        return score

#pretty much the same as other teas, but logic differs
class RedTea(Tea):
    def __init__(self):
        super().__init__("Red Tea", 90, 5)

    def match(self, prefs):
        score = 0
        score += 10 - abs(prefs.strength - 6)
        score += 10 - abs(prefs.sweetness - 5)
        score += 10 - abs(prefs.sourness - 2)
        return score


#class, that is choosing tea to recommend

class TeaRecommender:
    def __init__(self):
        self.teas = [BlackTea(), GreenTea(), RedTea()]
#method, that is using preferences, entered before to choose tea with best score be matching them with the others
    def recommend(self, prefs: Preferences):
        best_tea = None
        best_score = -1

        for tea in self.teas:
            score = tea.match(prefs)  # POLYMORPHISM
            if score > best_score:
                best_score = score
                best_tea = tea
#returning conclusion
        return best_tea, best_score