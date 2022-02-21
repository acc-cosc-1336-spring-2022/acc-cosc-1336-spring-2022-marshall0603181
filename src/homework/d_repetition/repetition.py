num = int(input('enter a number: '))

def get_factorial(num):
    factorial = 1
    if int(num) >= 1:
        for i in range(1, num+1):
            factorial = factorial * i
    print('The factorial of ', num, 'is', factorial)
# it works!

def sum_odd_numbers(num):
    print('The sum of all the odd numbers before ', num, 'is'\
        , sum_odd_numbers(num))