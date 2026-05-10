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
        super.__init__("Black Tea", 95, 4)

class GreenTea(Tea):
    def __init__(self):
        super.__init__("Green Tea", 80, 3)

class RedTea(Tea):
    def __init__(self):
        super.__init__("Red Tea", 90, 5)


class BrewTea:
    def __init__(self, tea, water_temp, water_time, sugar):
        self.tea = tea
        self.water_temp = water_temp
        self.water_time = water_time
        self.sugar = sugar

#giving the score to the tea

class Evaluator:
    def __init__(self, tea, water_temp, water_time, sugar):
        pass

#tea factory

class Factory:
    def create_tea(tea_type):
        if tea_type == "BlackTea":
            return BlackTea()
        elif tea_type == "GreenTea":
            return GreenTea()
        elif tea_type == "RedTea":
            return RedTea()
        else:
            raise Exception("Unknown tea type")

