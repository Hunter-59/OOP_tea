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

    def base_score(
            self,
            prefs,
            sugar,
            lemon,
            sweetness_mult,
            sourness_mult,
            bitterness_mult,
            strength_mult
    ):
        final_sweetness = self.sweetness + sugar.sweetness_bonus()
        final_sourness = self.sourness + lemon.sourness_bonus()
        final_bitterness = self.bitterness - lemon.bitterness_reduction()
        final_strength = self.strength

        score = 0

        score += (10 - abs(final_sweetness - prefs.sweetness)) * sweetness_mult
        score += (10 - abs(final_sourness - prefs.sourness)) * sourness_mult
        score += (10 - abs(final_bitterness - prefs.bitterness)) * bitterness_mult
        score += (10 - abs(final_strength - prefs.strength)) * strength_mult

        max_score = (
                10 * sweetness_mult +
                10 * sourness_mult +
                10 * bitterness_mult +
                10 * strength_mult
        )

        score = score / max_score * 50

        return score

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

    def match(self, prefs, sugar, lemon):
        score = self.base_score(
            prefs,
            sugar,
            lemon,
            sweetness_mult=1.0,
            sourness_mult=0.5,
            bitterness_mult=2.0,
            strength_mult=2.5
        )

        score += sugar.amount * 1.5

        return round(min(score, 50), 1)

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

    def match(self, prefs, sugar, lemon):
        score = self.base_score(
            prefs,
            sugar,
            lemon,
            sweetness_mult=0.7,
            sourness_mult=1.8,
            bitterness_mult=1.5,
            strength_mult=0.8
        )

        score -= sugar.amount * 2

        return round(max(score, 0), 1)


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

    def match(self, prefs, sugar, lemon):
        score = self.base_score(
            prefs,
            sugar,
            lemon,
            sweetness_mult=2.0,
            sourness_mult=1.2,
            bitterness_mult=0.7,
            strength_mult=1.3
        )

        score += lemon.amount * 2

        return round(min(score, 50), 1)


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