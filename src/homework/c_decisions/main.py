import decisions
from src.homework.c_decisions.decisions import get_faculty_rating

options = int(input())
total = int(input())

result = decisions.get_options_ratio(options, total)

print(get_faculty_rating(result))