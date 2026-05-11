from abc import ABC, abstractmethod

#creating classes

class Tea:
    @abstractmethod
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
    def __init__(self, tea, water_temp, water_time, sugar, lemon):
        self.tea = tea
        self.water_temp = water_temp
        self.water_time = water_time
        self.sugar = sugar
        self.lemon = lemon

    def describe(self):
        print(self.water_temp)
        print(self.water_time)
        print(self.sugar)
        print(self.lemon)

#giving the score to the tea

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

        #sugar analysis
        if brewedtea.sugar == 0:
            print("- unsweetened")
        elif brewedtea.sugar == 1:
            print("- a bit sweet")
        elif brewedtea.sugar == 2:
            print("- sweet")
        elif brewedtea.sugar >= 3:
            print("- very sweet")

        print("Also, the taste is going to be:")

        #temperature analysis
        temp_diff = brewedtea.water_temp - brewedtea.tea.op_temp
        if temp_diff <= -10:
            print("- weak and under-extracted due to insufficient water temperature.")
        elif temp_diff >= 10:
            print("- bitter and potentially burnt due to excessive water temperature.")
        else:
            print("- accurately extracted based on temperature.")

        #time analysis
        time_diff = brewedtea.water_time - brewedtea.tea.op_time
        if time_diff <= -1:
            print("- watery due to an insufficient brewing duration.")
        elif time_diff >= 2:
            print("- astringent and over-steeped due to an excessive brewing duration.")
        else:
            print("- well-balanced based on the brewing time.")

        #lemon analysis
        if brewedtea.lemon == True:
            print("- your tea is going to be a bit sour, perfect addition")

#tea factory

class Factory:
    @staticmethod
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