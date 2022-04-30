 
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
    
bottle1 = Bottle(473, "water")

print(bottle1.volume) # 473
print(bottle1.type_) # water