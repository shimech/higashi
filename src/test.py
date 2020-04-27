import unittest
from ex1.classify_triangle import classify_triangle
from pre2.between import between
from pre2.inc_digits import inc_digits
from ex2.tuple_list import tuple_list
from pre3.letter_n_gram_list import letter_n_gram_list
from pre3.inc_freq import inc_freq
from ex3.transpose import transpose


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


class TestLetterNGramList(unittest.TestCase):
    def test_letter_n_gram_list(self):
        ss = [
            "今日は",
            "今日は",
            "今日は",
            "今日は",
            "abcd",
            "abcd",
            "abcd",
            "",
            ""
        ]
        ns = [
            1,
            2,
            3,
            4,
            3,
            4,
            5,
            1,
            2
        ]
        expecteds = [
            ["今", "日", "は"],
            ["今日", "日は"],
            ["今日は"],
            [],
            ["abc", "bcd"],
            ["abcd"],
            [],
            [],
            []
        ]

        for s, n, expected in zip(ss, ns, expecteds):
            self.assertEqual(expected, letter_n_gram_list(s, n))


class TestIncFreq(unittest.TestCase):
    def test_inc_freq(self):
        ss = [
            "Is this a pen?",
            "Hello."
        ]
        d = {"a": 0, "e": 1, "s": 2, ".": 3}
        expecteds = [
            {"a": 1, "e": 2, "s": 4, ".": 3},
            {"a": 1, "e": 3, "s": 4, ".": 4},
        ]

        for s, expected in zip(ss, expecteds):
            inc_freq(s, d)
            self.assertEqual(expected, d)


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
