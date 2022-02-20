print('Homework 3 menu')
choice = int(input('(1) Factorial (2) Sum odd numbers (3) Exit: '))
import repetition
from repetition import num
# choice has to do with 'Homework 3 menu'.
if choice == 1:
    if num > 0 and num < 10:
        repetition.get_factorial(int(num))
    else:
        print('Error')
if choice == 2:
    choice = int(input('Sorry that function is not yet working. Please try again: '))
if choice == 3:
    exit('Exiting...')

# choice2 has to do with the question 'Do you want to exit? y or n: '.
choice2 = str(input('Do you wish to continue? y or n: '))
if choice2 == 'n':
    exit('Exiting...')
elif choice2 == 'y':
    from repetition import num
    repetition.get_factorial(num)
if choice == 1 and num > 0 and num < 10:
    repetition.get_factorial(num)
else:
    print('Error')
    
if choice == 2:
    choice = int(input('Sorry that function is not yet working. Please try again: '))
if choice == 3:
    exit('Exiting...')


#elif int(choice) == 2:
#from repetition import num
#while num < 0 and num > 100
#from repetition import num
#repetition.sum_odd_numbers(num)