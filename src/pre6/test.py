import unittest
from find_max_indices import find_max_indices
from drop_first import drop_first


class TestFindMaxIndices(unittest.TestCase):
    def test_find_max_indices(self):
        Ms = [[[1, 2, 3], [9, 8, 7, 6], [4, 5]]]
        expecteds = [(1, (0, 9))]

        for M, expected in zip(Ms, expecteds):
            self.assertEqual(expected, find_max_indices(M))


class TestDropFirst(unittest.TestCase):
    def test_drop_first(self):
        iterables = [[1, 2, 3]]
        expecteds = [[2, 3]]

        for iterable, expected in zip(iterables, expecteds):
            self.assertEqual(expected, list(drop_first(iterable)))


if __name__ == "__main__":
    unittest.main()
