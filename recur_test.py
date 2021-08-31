import random
import unittest
from recur_binary_search import binary_search

from random import choice


class TestCase(unittest.TestCase):

    # def test_true_recursion(self):
    #     array = [1, 2, 7, 12, 43, 44, 54, 100, 124, 147]
    #     n = choice(array)
    #     print(f"Random numbers: {n}")
    #     result = binary_search(array, n)
    #     self.assertTrue(result)

    def test_random_recursion(self):
        array = [1, 2, 7, 12, 43, 44, 54, 100, 124, 147]
        false_array = [i for i in range(1, 150)]

        for n in false_array:
            result = binary_search(array, n)
            if n in array:
                self.assertTrue(result)
                print("Trouvé")
            else:
                self.assertFalse(result)
                print("Pas dedans")


if __name__ == '__main__':
    unittest.main()