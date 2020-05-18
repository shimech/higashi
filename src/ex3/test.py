import unittest
from transpose import transpose


class TestTranspose(unittest.TestCase):
    def test_transpose(self):
        Ms = [
            [[1, 2, 3], [4, 5, 6]],
            [[0]],
            [[1, 2, 3]],
            [[1], [2], [3], [4]]
        ]
        expecteds = [
            [[1, 4], [2, 5], [3, 6]],
            [[0]],
            [[1], [2], [3]],
            [[1, 2, 3, 4]]
        ]

        for M, expected in zip(Ms, expecteds):
            self.assertEqual(expected, transpose(M))


if __name__ == "__main__":
    unittest.main()
