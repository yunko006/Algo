import unittest
from unittest import result
from binary_search import binary_search

from random import choice

class TestCase(unittest.TestCase):

    def test_iter_binary(self):
        array = [1, 2, 7, 12, 43, 44, 54, 100, 124, 147]

        for n in array:
            result = binary_search(array, n)
            self.assertTrue(result)

    def test_false_value(self):
        array = [1, 2, 7, 12, 43, 44, 54, 100, 124, 147]
        false_array = [3, 8, 55, 101, 116, 150]

        for n in false_array:
            result = binary_search(array, n)
            self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()