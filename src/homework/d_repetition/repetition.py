num = int(input('enter a number: '))

def get_factorial(num):
    factorial = 1
    if int(num) >= 1:
        for i in range(1, num+1):
            factorial = factorial * i
    print('the factorial of', num, 'is', factorial)
# it works!
#num = int(input('enter number: '))
#def sum_odd_numbers(num):
#    while num != 0:
#        print(num)
#        num = 0
