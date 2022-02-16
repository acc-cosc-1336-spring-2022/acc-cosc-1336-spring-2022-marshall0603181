
from webbrowser import get

num1 = float(input())
num2 = float(input())

def get_options_ratio(num1, num2):
    return num1 + num2

x = float(get_options_ratio(num1, num2))


def get_faculty_rating():
    return x
if x >= 0.9 or x == 1:
    print('Excellent')
if x >= 0.8:
    print('Very Good')
if x >= 0.7:
    print('Good')
if x >= 0.6:
    print('Needs Improvement')
if 0 >= x <= 0.59:
    print('Unacceptable')