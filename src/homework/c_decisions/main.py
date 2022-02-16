import decisions
#from decisions import get_faculty_rating
#from decisions import get_options_ratio

options = float(input("input 'options' value: "))
total = float(input("input 'total' value: "))

result = decisions.get_options_ratio(options, total)

print(result)