import unittest

from src.examples.g_lists_and_tuples.lists import test_config
from src.examples.g_lists_and_tuples import lists

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
    def test_loop_w_for(self):
        self.asserEqual(1, lists.loop_list_w_for(1))
    def test_loop_w_while(self):
        self.assertEqual(1, lists.loop_list_w_while(1))

    def test_append_item_to_list(self):
        list1 = []
        lists.append_item_to_list("C++", list1)
        lists.append_item_to_list("Python", list1)
        expected_list = ["C++", "Python"]
        
