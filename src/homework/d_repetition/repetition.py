num = int(input('enter a number: '))

def get_factorial(num):
    factorial = 1
    if int(num) >= 1:
        for i in range(1, num+1):
            factorial = factorial * i
            fact = "The factorial of {} is {}"
    print(fact.format(num, factorial))
get_factorial(num)
# it works!

#def sum_odd_numbers(num):
#
 #   sum_odd_numbers(int(num))