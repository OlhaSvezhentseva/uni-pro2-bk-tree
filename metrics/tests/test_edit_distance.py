# Olha Svezhentseva
# 16.08.2022

import unittest
from metrics.edit_distance import EditDistanceCalculator


class DistanceTestSuite(unittest.TestCase):
    """A class to test EditDistanceCalculator"""
    def setUp(self):
        self.calculator = EditDistanceCalculator()

    def test_example(self):
        actual = self.calculator.compute_distance("vogel", "löffel")
        expected = 4
        self.assertEqual(actual, expected)

    def test_symmetry(self):
        one_direct = self.calculator.compute_distance("vogel", "löffel")
        other_direct = self.calculator.compute_distance("löffel", "vogel")
        self.assertEqual(one_direct, other_direct)

    def test_triangle(self):
        # (x, y) <= d(x, z) + d(z, y)
        single = self.calculator.compute_distance("hinein", "haben")
        compound = self.calculator.compute_distance("hinein", "ein") + self.calculator.compute_distance("ein", "haben")
        self.assertLessEqual(single, compound)

    def test_empty_string(self):
        actual = self.calculator.compute_distance("", "löffel")
        expected = 6
        self.assertEqual(actual, expected)

    def test_empty_strings(self):
        actual = self.calculator.compute_distance("", "")
        expected = 0
        self.assertEqual(actual, expected)

    def test_exact_match(self):
        actual = self.calculator.compute_distance("haus", "haus")
        expected = 0
        self.assertEqual(actual, expected)

