import unittest

import utils

class TestUtils(unittest.TestCase):

    def metoda(neco=None, nic=False):
        pass

    def test_contains(self):
        cases = [
            [ "automobil", 0, "auto" ],
            [ "mojeauto", 4, "auto" ],
            [ "mojeauto", 5, "uto" ],
        ]

        for c in cases:
            self.assertTrue(utils.contains(*c), msg=f"{c}")
