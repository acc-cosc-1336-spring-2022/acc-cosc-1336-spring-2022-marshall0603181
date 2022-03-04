import random

def test_config():
    return True

def local_variable(val0):
    val = val0
    val0 = 100
    return val
    

def main(val0):
    val = 0
    local_variable(val0)
    return val

VAL3 = 10
def use_global():
    #VAL3 = 5
    #print(VAL3)
    global VAL3
    VAL3 = 100

#print('global call', VAL3)

def get_random_number(min, max): # user defined function with python library
    return random.randint(min, max)
cnt = 0
def display_random_numbers(min, max, cnt):
    for i in range(cnt):
        print(random.randint(min, max))



#random.seed(10)