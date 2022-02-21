num = int(input('enter a number: '))

def get_factorial(num):
    factorial = 1
    if int(num) >= 1:
        for i in range(1, num+1):
            factorial = factorial * i
    print('The factorial of ', num, 'is', factorial)
# it works!

numbers = range(0, 10)

def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if int(num) % 2 == 1:
            total += int(num)
    print(total)