import unittest

from src.examples.h_strings.strings import test_config
from src.examples.h_strings.strings import concat_strings

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_concat_strings(self):
        self.assertEqual("john doe", concat_strings("john ", "doe"))