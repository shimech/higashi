import unittest
from src.tuple_list import tuple_list


class TestTupleList(unittest.TestCase):
    def test_tuple_list(self):
        lps = [
            [("book", 3), ("pen", 5), ("eraser", 2), ("pen", 1), ("book", 10)],
            [("book", 3), ("pen", 5), ("eraser", 2), ("pen", 1), ("book", 10)],
            [("book", 3), ("pen", 5), ("eraser", 2), ("pen", 1), ("book", 10)]
        ]
        xs = [
            "pen",
            "eraser",
            "apple"
        ]
        expecteds = [
            [5, 1],
            [2],
            []
        ]

        for lp, x, expected in zip(lps, xs, expecteds):
            self.assertEqual(expected, tuple_list(lp, x))


if __name__ == "__main__":
    unittest.main()
