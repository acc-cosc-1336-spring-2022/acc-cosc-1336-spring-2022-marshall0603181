
from webbrowser import get


num1 = int(input())
num2 = int(input())

def get_options_ratio(num1, num2):
    return num1 + num2

x = int(get_options_ratio(num1, num2))


def get_faculty_rating():
    return x
if 0.9 >= x > 1:
    print('Excellent')
if x > 0.8:
    print('Very Good')
if x > 0.7:
    print('Good')
if x > 0.6:
    print('Needs Improvement')
if 0 > x > 0.59:
    print('Unacceptable')