num = int(input('enter a number: '))
def get_factorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial * i
        print('the factorial of', num, 'is', factorial)
get_factorial(num)
# it works but in a weird way
num = int(input('enter number: '))
def sum_odd_numbers(num):
    while num != 0:
        print(num)
        num = 0
sum_odd_numbers(num)