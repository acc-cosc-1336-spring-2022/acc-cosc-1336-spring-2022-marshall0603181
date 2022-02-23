def get_factorial(num):
    factorial = 1
    for i in range(num + 1):
        if(i > 0):
            factorial *= i
    return factorial
# it works!
# we need to figure out a way to add only the odd numbers 
# up to but not exceeding num
# in order to use a while loop, we need to make a control
# variable that will prevent the loop from being infinite.
def sum_odd_numbers(num):
    result = 0
    i = 0
    while i <= num:
        if((i % 2) == 1):
            result += i
        i += 1
    return result
