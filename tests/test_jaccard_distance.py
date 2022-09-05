# Olha Svezhentseva
# 16.08.2022

import unittest
from bk_program.metrics import JaccardDistanceCalculator


class JaccardDistanceTestSuite(unittest.TestCase):
    """A class to test JaccardDistanceCalculator."""

    def setUp(self):
        self.calculator = JaccardDistanceCalculator()

    def test_general(self):
        actual = self.calculator.compute_distance("night", "nacht")
        expected = 0.86
        self.assertEqual(actual, expected)

    def test_symmetry(self):
        one_direct = self.calculator.compute_distance("night", "nacht")
        other_direct = self.calculator.compute_distance("nacht", "night")
        self.assertEqual(one_direct, other_direct)

    def test_triangle(self):
        # (x, y) <= d(x, z) + d(z, y)
        single = self.calculator.compute_distance("hinein", "haben")
        compound = self.calculator.compute_distance("hinein", "ein") \
            + self.calculator.compute_distance("ein", "haben")
        self.assertLessEqual(single, compound)

    def test_empty_string(self):
        actual = self.calculator.compute_distance("", "nacht")
        expected = 1.0
        self.assertEqual(actual, expected)

    def test_empty_strings(self):
        actual = self.calculator.compute_distance("", "")
        expected = 0
        self.assertEqual(actual, expected)

    def test_exact_match(self):
        actual = self.calculator.compute_distance("haus", "haus")
        expected = 0
        self.assertEqual(actual, expected)

