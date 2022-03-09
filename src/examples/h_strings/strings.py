#import random
from re import S


def test_config():
    return True

#x = random.randint(0, 10)

#def hello_world():
#   hello = 'hello world' #string
#   print(hello)
#   print(hello[x])

def loop_string(str):
    for c in str("hello"):
        print(c)

def concat_strings(str1, str2):
    return str1 + str2