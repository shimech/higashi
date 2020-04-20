import unittest
from src.tuple_list import tuple_list
from src.letter_n_gram_list import letter_n_gram_list


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


if __name__ == "__main__":
    unittest.main()
