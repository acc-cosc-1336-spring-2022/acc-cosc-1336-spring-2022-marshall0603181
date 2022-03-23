import unittest

from src.examples.g_lists_and_tuples.lists import test_config
from src.examples.g_lists_and_tuples.lists import loop_list_w_for
from src.examples.g_lists_and_tuples.lists import loop_list_w_while

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())
    def test_loop_w_for(self):
        self.asserEqual(1, loop_list_w_for(1))
    def test_loop_w_while(self):
        self.assertEqual(1, loop_list_w_while(1))