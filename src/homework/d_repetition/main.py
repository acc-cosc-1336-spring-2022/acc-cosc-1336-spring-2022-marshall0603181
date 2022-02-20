from repetition import get_factorial
from repetition import sum_odd_numbers
print('Homework 3 menu')
choice = int(input('1-Factorial 2-Sum odd numbers 3-Exit: '))
if choice == 1:
    num = int(input('enter number: '))
    get_factorial(num)
elif choice == 2:
    num = int(input('enter number: '))
    sum_odd_numbers(num)
elif choice == 3:
    exit()