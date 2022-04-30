import unittest

from src.homework.j_classes.class_a import die

class Test_Config(unittest.TestCase):
    def test_get_rolled_value(self):
        self.assertEqual(die.get_rolled_value(self), [1, 2, 3, 4, 5, 6])