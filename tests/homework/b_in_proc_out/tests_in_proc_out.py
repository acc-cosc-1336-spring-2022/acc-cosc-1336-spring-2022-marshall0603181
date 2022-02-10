import unittest

'''
The file at /src/homework/b_in_proc_out/output has 
the function multiply_numbers.
'''

from src.homework.b_in_proc_out.output import multiply_numbers

class Test_Config(unittest.TestCase):

    def test_multiply_numbers_1(self):
        self.assertEqual(25, multiply_numbers(5 , 5))

    def test_multiply_numbers_2(self):
        self.assertEqual(100, multiply_numbers(10 , 10))

    def test_multiply_number_3(self):
        self.assertEqual(36, multiply_numbers(6,6))