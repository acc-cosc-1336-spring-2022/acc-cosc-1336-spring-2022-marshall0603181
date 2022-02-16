import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):
    def test_get_options_ratio(self):
        self.assertEqual(0.25, 5 / 20)
        self.assertEqual(0.5, 10 / 20)
    
    def test_get_faculty_rating(self):
        self.assertEqual(1, 6.0 / 6.0)
        self.assertEqual(0.75, 3 / 4)
        
        if get_faculty_rating == .91:
            return 'Excellent'
        if get_faculty_rating == .85:
            return 'Very Good'
        if get_faculty_rating == .71:
            return 'Good'
        if get_faculty_rating == .66:
            return 'Needs Improvement'
        if get_faculty_rating == .45:
            return 'Unacceptable'