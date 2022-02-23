def get_factorial(num):
    factorial = 1
    if int(num) >= 1:
        for i in range(1, num+1):
            factorial = factorial * i
    print(factorial)
# it works!
# we need to figure out a way to add only the odd numbers 
# up to but not exceeding num
# in order to use a while loop, we need to make a control
# variable that will prevent the loop from being infinite.
def sum_odd_numbers(num):
    rem = num % 2
    while rem == 0:
        print(num)
        break
