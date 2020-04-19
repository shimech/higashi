import sys
import unittest
from src.between import between
from src.inc_digits import inc_digits


class TestBetween(unittest.TestCase):
    def test_between(self):
        lns = [
            [20, 10, 50, 30, 40],
            ["a", "b", "c", "d", "e"]
        ]
        xs = [
            10,
            "e"
        ]
        ys = [
            30,
            "c"
        ]
        expecteds = [
            [10, 50, 30],
            ["c", "d", "e"]
        ]

        for ln, x, y, expected in zip(lns, xs, ys, expecteds):
            self.assertEqual(expected, between(ln, x, y))


class TestIncDigits(unittest.TestCase):
    def test_inc_digits(self):
        ss = ["12", "457"]
        ns = [5, 5]
        expecteds = ["67", "902"]

        for s, n, expected in zip(ss, ns, expecteds):
            self.assertEqual(expected, inc_digits(s, n))


if __name__ == "__main__":
    unittest.main()
