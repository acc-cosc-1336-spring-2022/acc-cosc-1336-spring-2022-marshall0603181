import repetition
# choice has to do with 'Homework 3 menu'.
choice2 = 'y'
while choice2 == 'y':
    print('Homework 3 Menu')
    choice = int(input('\n(1) Factorial \n(2) Sum odd numbers \n(3) Exit \n\n '))
    if choice == 1:
        num = int(input('enter number greater than 0 and less than 10: '))
        if num > 0 and num < 10:
            print(repetition.get_factorial(num))
        while num <= 0 or num >= 10:
            print('Invalid entry')
            num = int(input('enter number greater than 0 and less than 10: '))
            if num > 0 and num < 10:
                print(repetition.get_factorial(num))
    elif choice == 2:
        num = int(input('enter a number: '))
        print(repetition.sum_odd_numbers(num))
    elif choice == 3:
        exit('Exiting...')
    else:
        print('Error')
    choice2 = str(input('Do you wish to continue? y or n: '))

# choice2 has to do with the question 'Do you want to exit? y or n: '.
if choice2 == 'n':
    exit('Exiting...')