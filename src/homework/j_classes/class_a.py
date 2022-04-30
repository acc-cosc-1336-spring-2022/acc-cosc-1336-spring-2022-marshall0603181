import random

class die:

    def roll(self):
        random.randint(1, 7)

    def get_rolled_value(self):
        return self.roll()

    def __str__(self):
        print("The rolled value is " + str(self.get_rolled_value()))