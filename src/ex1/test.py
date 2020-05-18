import unittest
from classify_triangle import classify_triangle


class TestClassifyTriangle(unittest.TestCase):
    def test_classify_triangle(self):
        args = [
            [3, 6, 5],
            [3, 4, 5],
            [4, 3, 3],
            [1, 1, 3],
            [1, 2, 1],
            [3, 2, 1]
        ]
        expecteds = [
            3,
            2,
            1,
            0,
            0,
            0
        ]

        for arg, expected in zip(args, expecteds):
            a, b, c = arg
            self.assertEqual(expected, classify_triangle(a, b, c))


if __name__ == "__main__":
    unittest.main()
