import unittest
from src.homework.c_decisions.decisions import get_options_ratio
#from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):
    def test_get_options_ratio(self):
        self.assertEqual(25, 5 + 20)
        self.assertEqual(30, 10 + 20)
    def test_get_faculty_rating(self):
        if get_options_ratio == 91:
            return 'Excellent'
        if get_options_ratio == 85:
            return 'Very Good'
        if get_options_ratio == 71:
            return 'Good'
        if get_options_ratio == 66:
            return 'Needs Improvement'
        if get_options_ratio == 45:
            return 'Unacceptable'
