#creating classes

class Tea:
    def __init__(self, name, op_temp, op_time):
        self.name = name
        self.op_temp = op_temp
        self.op_time = op_time

    def describe(self):
        print(self.name)
        print(self.op_temp)
        print(self.op_time)

class BlackTea(Tea):
    def __init__(self):
        super().__init__("Black Tea", 95, 4)

class GreenTea(Tea):
    def __init__(self):
        super().__init__("Green Tea", 80, 3)

class RedTea(Tea):
    def __init__(self):
        super().__init__("Red Tea", 90, 5)


class BrewTea:
    def __init__(self, tea, water_temp, water_time, sugar, lemon, milk_ratio):
        self.tea = tea
        self.water_temp = water_temp
        self.water_time = water_time
        self.sugar = sugar
        self.lemon = lemon
        self.milk_ratio = milk_ratio

    def describe(self):
        print(self.water_temp)
        print(self.water_time)
        print(self.sugar)
        print(self.lemon)
        print(self.milk_ratio)

#giving the score to the tea

class Conclusion:
    def score(self, brewedtea):
        score = 100

        score -= abs(brewedtea.tea.op_temp - brewedtea.water_temp) / brewedtea.tea.op_temp * 100
        score -= abs(brewedtea.tea.op_time - brewedtea.water_time) / brewedtea.tea.op_time * 100

        print("Score of your tea: ", score)

    class Conclusion:
        @staticmethod
        def score(brewedtea):
            score = 100

            score -= abs(brewedtea.tea.op_temp - brewedtea.water_temp) / brewedtea.tea.op_temp * 100
            score -= abs(brewedtea.tea.op_time - brewedtea.water_time) / brewedtea.tea.op_time * 100

            print("Score of your tea: ", score)

        @staticmethod
        def description(brewedtea):
            print("Your tea will be:")

            # Sugar analysis
            if brewedtea.sugar == 0:
                print("- unsweetened")
            elif brewedtea.sugar == 1:
                print("- a bit sweet")
            elif brewedtea.sugar == 2:
                print("- sweet")
            elif brewedtea.sugar >= 3:
                print("- very sweet")

            print("Also, the taste is going to be:")

            # Temperature analysis
            temp_diff = brewedtea.water_temp - brewedtea.tea.op_temp
            if temp_diff <= -10:
                print("- weak and under-extracted due to insufficient water temperature.")
            elif temp_diff >= 10:
                print("- bitter and potentially burnt due to excessive water temperature.")
            else:
                print("- accurately extracted based on temperature.")

            # Time analysis
            time_diff = brewedtea.water_time - brewedtea.tea.op_time
            if time_diff <= -1:
                print("- watery due to an insufficient brewing duration.")
            elif time_diff >= 2:
                print("- astringent and over-steeped due to an excessive brewing duration.")
            else:
                print("- well-balanced based on the brewing time.")

            # Lemon and Milk analysis
            if brewedtea.lemon and brewedtea.milk_ratio > 0:
                print(
                    "- unpalatable and curdled. The acidity of the lemon has reacted adversely with the milk proteins.")
            else:
                if brewedtea.lemon:
                    print("- citrusy and acidic due to the addition of lemon.")

                if brewedtea.milk_ratio > 0:
                    if brewedtea.milk_ratio <= 0.2:
                        print("- creamy with a standard dash of milk.")
                    elif brewedtea.milk_ratio <= 0.5:
                        print("- quite milky, which will significantly dilute the primary tea flavour.")
                    else:
                        print("- predominantly milk, entirely overwhelming the tea infusion.")


#tea factory

class Factory:
    def create_tea(tea_type):
        tea_type = tea_type.lower()

        if tea_type == "black":
            return BlackTea()
        elif tea_type == "green":
            return GreenTea()
        elif tea_type == "red":
            return RedTea()
        else:
            raise Exception("Unknown tea type")

