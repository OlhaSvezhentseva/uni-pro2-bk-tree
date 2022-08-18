import unittest
from distance import DistanceCalculator


DIST = DistanceCalculator()


class DistanceTestSuite(unittest.TestCase):

    def testExample1(self):
        actual = DIST.compute_distance("vogel", "löffel")
        expected = 4
        self.assertEqual(actual, expected)

    def test_symmetry(self):
        one_direct = DIST.compute_distance("vogel", "löffel")
        other_direct = DIST.compute_distance("löffel", "vogel")
        self.assertEqual(one_direct, other_direct)

    def test_triangle(self):
        # (x, y) <= d(x, z) + d(z, y)
        single = DIST.compute_distance("hinein", "haben")
        compound = DIST.compute_distance("hinein", "ein") + DIST.compute_distance("ein", "haben")
        self.assertLessEqual(single, compound)

    def test_empty_string(self):
        actual = DIST.compute_distance("", "löffel")
        expected = 6
        self.assertEqual(actual, expected)

    def test_empty_strings(self):
        actual = DIST.compute_distance("", "")
        expected = 0
        self.assertEqual(actual, expected)

    def test_exact_match(self):
        actual = DIST.compute_distance("haus", "haus")
        expected = 0
        self.assertEqual(actual, expected)