import random

class Die:

    def roll(self):
        return random.randint(1, 6)

    def __str__(self):
        print("The roll is", str(self.roll()))

die = Die()
