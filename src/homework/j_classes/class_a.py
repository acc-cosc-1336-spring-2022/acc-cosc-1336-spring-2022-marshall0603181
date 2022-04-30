import random

class Die:

    def roll(self):
        __roll_value = random.randint(1, 6)
        return __roll_value

    def get_rolled_value(self):
        return self.roll()

    def __str__(self):
        print("You rolled {}!".format(self.get_rolled_value()))

die = Die()
