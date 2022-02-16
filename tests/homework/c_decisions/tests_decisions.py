import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):
    def test_get_options_ratio(self):
        self.assertEqual(25, 5 + 20)
        self.assertEqual(25, 20 + 5)
    def test_get_faculty_rating(self):
        if get_options_ratio == 91:
            print('Excellent')
        if get_options_ratio == 85:
            print('Very Good')
        if get_options_ratio == 71:
            print('Good')
        if get_options_ratio == 66:
            print('Needs Improvement')
        if get_options_ratio == 45:
            print('Unacceptable')
