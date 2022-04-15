from audioop import add
from os import remove
import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance_matrix
from src.homework.i_dictionaries_sets.dictionary import get_p_distance
from src.homework.i_dictionaries_sets.dictionary import add_inventory
from src.homework.i_dictionaries_sets.dictionary import remove_inventory_widget

class Test_Config(unittest.TestCase):
    def test_get_p_distance(self):
        # test that get_p_distance returns 0.4 when given list1 and list2
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']
        self.assertEqual(0.4, get_p_distance(list1, list2))

    def test_get_p_distance_matrix(self):
        # test that get_p_distance_matrix returns p_distance_matrix when given a dataset
        dataset = [ ['T','T','T','C','C','A','T','T','T','A'],
                    ['G','A','T','T','C','A','T','T','T','C'],
                    ['T','T','T','C','C','A','T','T','T','T'],
                    ['G','T','T','C','C','A','T','T','T','A']   ]
        p_distance_matrix = [   [0.0, 0.4, 0.1, 0.1],
                                [0.4, 0.0, 0.4, 0.3],
                                [0.1, 0.4, 0.0, 0.2],
                                [0.1, 0.3, 0.2, 0.0]    ]
        self.assertEqual(p_distance_matrix, get_p_distance_matrix(dataset))

    def test_add_inventory(self):
        dictionary1 = dict({'widget_name':10})
        self.assertEqual(10, add_inventory(dictionary1['widget_name']))
        self.assertEqual(35, add_inventory({'Widget1':25}))
        self.assertEqual(25, add_inventory({'Widget1':-10}))

    def test_remove_inventory_widget(self):
        self.assertEqual(1, remove_inventory_widget())
        self.assertEqual(True, remove_inventory_widget())