import random
class Die:
    def roll():
        roll_value = random.randint(1,7)
        return roll_value
    def get_rolled_value(roll_value):
        print("The rolled value is ", roll_value,".")
        
    