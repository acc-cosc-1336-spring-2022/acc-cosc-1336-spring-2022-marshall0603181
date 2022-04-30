import random
class die:
    def roll(self):
        self.roll_value = random.randint(1, 7)
    def get_rolled_value(self):
        return self.roll_value
    def __str__(self):
        return "The rolled value is " + self.get_rolled_value