from abc import ABC, abstractmethod

#user preferences
class Preferences:
    def __init__(self, sweetness, sourness, bitterness, strength):
        self.sweetness = sweetness
        self.sourness = sourness
        self.bitterness = bitterness
        self.strength = strength


#sugar and lemon modifiers
class Sugar:
    def __init__(self, amount: int):
        self.amount = amount

    def sweetness_bonus(self):
        return self.amount * 1.5


class Lemon:
    def __init__(self, amount: int):
        self.amount = amount

    def sourness_bonus(self):
        return self.amount * 2

    def bitterness_reduction(self):
        return self.amount * 0.5


#abstract tea class
class Tea(ABC):
    def __init__(
        self,
        name,
        sweetness,
        sourness,
        bitterness,
        strength,
        brew_temp,
        brew_time
    ):

        self.name = name
        self.sweetness = sweetness
        self.sourness = sourness
        self.bitterness = bitterness
        self.strength = strength
        self.brew_temp = brew_temp
        self.brew_time = brew_time

    @abstractmethod
    def get_multipliers(self):
        pass

    def match(self, prefs, sugar, lemon):

        final_sweetness = self.sweetness + sugar.sweetness_bonus()
        final_sourness = self.sourness + lemon.sourness_bonus()
        final_bitterness = self.bitterness - lemon.bitterness_reduction()
        final_strength = self.strength

        score = 0
        multipliers = self.get_multipliers()

        score += (10 - abs(final_sweetness - prefs.sweetness)) * multipliers["sweetness"]
        score += (10 - abs(final_sourness - prefs.sourness)) * multipliers["sourness"]
        score += (10 - abs(final_bitterness - prefs.bitterness)) * multipliers["bitterness"]
        score += (10 - abs(final_strength - prefs.strength)) * multipliers["strength"]

        max_score = (10 * multipliers["sweetness"] + 10 * multipliers["sourness"] +
                     10 * multipliers["bitterness"] + 10 * multipliers["strength"])

        score = score / max_score * 50

        return round(score, 1)

    #brewing info
    def brew_info(self):
        return f"{self.brew_temp}°C, {self.brew_time} min"


#tea classes
class BlackTea(Tea):
    def __init__(self):
        super().__init__(
            "Black Tea",
            sweetness=2,
            sourness=1,
            bitterness=7,
            strength=9,
            brew_temp=95,
            brew_time=4
        )

    def get_multipliers(self):
        return {
            "sweetness": 1.0,
            "sourness": 0.5,
            "bitterness": 2.0,
            "strength": 2.5
        }


#------------------------------------------------------------------------
class GreenTea(Tea):
    def __init__(self):
        super().__init__(
            "Green Tea",
            sweetness=3,
            sourness=4,
            bitterness=5,
            strength=4,
            brew_temp=80,
            brew_time=3
        )

    def get_multipliers(self):
        return {
            "sweetness": 0.7,
            "sourness": 1.8,
            "bitterness": 1.5,
            "strength": 0.8
        }


#------------------------------------------------------------------------
class RedTea(Tea):
    def __init__(self):
        super().__init__(
            "Red Tea",
            sweetness=5,
            sourness=2,
            bitterness=3,
            strength=6,
            brew_temp=90,
            brew_time=5
        )

    def get_multipliers(self):
        return {
            "sweetness": 2.0,
            "sourness": 1.2,
            "bitterness": 0.7,
            "strength": 1.3
        }


#tea recommender system
class TeaRecommender:
    def __init__(self):
        self.teas = [BlackTea(), GreenTea(), RedTea()]

    def recommend(self, prefs):

        best_tea = None
        best_score = -1

        best_sugar = 0
        best_lemon = 0

        #trying different combinations
        for tea in self.teas:
            for sugar_amount in range(0, 4):
                for lemon_amount in range(0, 3):

                    sugar = Sugar(sugar_amount)
                    lemon = Lemon(lemon_amount)

                    score = tea.match(prefs, sugar, lemon)

                    if score > best_score:

                        best_score = score
                        best_tea = tea

                        best_sugar = sugar_amount
                        best_lemon = lemon_amount

        return best_tea, best_score, best_sugar, best_lemon