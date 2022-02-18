option = float(input("input dividend: "))
total = float(input("input divisor: "))

def get_options_ratio(option, total):
    return option / total

x = get_options_ratio(option, total)

def get_faculty_rating(x):
    return x
if x >= 0.9 or x == 1:
    print('Excellent')
elif x >= 0.8 and x < 0.9:
    print('Very Good')
elif x >= 0.7 and x < 0.8:
    print('Good')
elif x >= 0.6 and x < 0.7:
    print('Needs Improvement')
else: 
    0 > x <= 0.59 and x < 0.6
    print('Unacceptable')
print('Numerical rating is: ', x*100,'%')