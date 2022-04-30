import unittest

from src.homework.j_classes.class_a import die

class Test_Config(unittest.TestCase):

    def test_roll1(self):
        self.assertIn(die.get_rolled_value(), [1,2,3,4,5,6])

    def test_roll2(self):
        self.assertIn(die.get_rolled_value(), [1,2,3,4,5,6])

    def test_roll3(self):
        self.assertIn(die.get_rolled_value(), [1,2,3,4,5,6])

    def test_roll4(self):
        self.assertIn(die.get_rolled_value(), [1,2,3,4,5,6])
    
    def test_roll5(self):
        self.assertIn(die.get_rolled_value(), [1,2,3,4,5,6])