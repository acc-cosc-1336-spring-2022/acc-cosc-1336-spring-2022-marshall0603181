print('Homework 3 Menu')
choice = int(input('\n(1) Factorial \n(2) Sum odd numbers \n(3) Exit \n\n '))
import repetition
num = int(input('enter a number: '))
# choice has to do with 'Homework 3 menu'.
if choice == 1 and num > 0 and num < 10:
    print(repetition.get_factorial(num))
elif choice == 2:
    print(repetition.sum_odd_numbers(num))
elif choice == 3:
    exit('Exiting...')
else:
    print('Error')

# choice2 has to do with the question 'Do you want to exit? y or n: '.
choice2 = str(input('Do you wish to continue? y or n: '))
if choice2 == 'n':
    exit('Exiting...')
elif choice2 == 'y':
    print('Homework 3 Menu')
    choice = (int(input('(1) Factorial (2) Sum odd numbers (3) Exit: ')))
else:
    print('Error')


#elif int(choice) == 2:
#from repetition import num
#while num < 0 and num > 100
#from repetition import num
#repetition.sum_odd_numbers(num)