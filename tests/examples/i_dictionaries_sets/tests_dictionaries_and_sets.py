import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_dictionary_create(self):
        phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        expected_dictionary = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}

        self.assertEqual(phonebook, expected_dictionary)

    def test_dictionary_update_value(self):
        phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        phonebook['Katie'] = "555-4444"
        self.assertEqual(phonebook['Katie'], '555-4444')

    def test_new_dictionary_value(self):
        phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        phonebook['Joe'] = '555-5555'
        self.assertEqual(phonebook['Joe'], '555-5555')

    def test_dictionary_delete_key_value_pair(self):
        phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        del phonebook['Katie']
        expected_dictionary = {'Chris':'555-1111', 'Joanne':'555-3333'}
        self.assertEqual(phonebook, expected_dictionary)

    def test_dictionary_clear_method(self):
        phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        pass

    def test_dictionary_get_item(self):
        phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        v = phonebook.get('Chris')
        self.assertEqual(v, "555-1111")
        v = phonebook.get('chris')
        self.assertEqual(v, None) #Default value is none

    def test_dictionary_pop(self):
        phonebook = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        expected_dictionary = {'Chris':'555-1111', 'Katie':'555-2222', 'Joanne':'555-3333'}
        v = phonebook.pop('Katie')
        self.assertEqual(v, '555-2222')
        self.assertEqual(expected_dictionary, phonebook)

        def test(self):
            pass