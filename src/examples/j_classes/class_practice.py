
class Person:
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase

user = Person(25, 80, 177, "Jon", "Snow", "You know nothing, Jon Snow")

print(user.catch_phrase)

class Bottle:
    def __init__(self, volume, type_):
        self.volume = volume
        self.type_ = type_

    def pour(self):
        print("Pouring...")

    def fill(self):
        print("Filling...")

    def recycle(self):
        print("Recycling...")
    
bottle1 = Bottle()

print(bottle1.volume) # 473
print(bottle1.type_) # water
bottle1.pour() # Pouring...
bottle1.fill() # Filling...
bottle1.recycle() # Recycling...