import unittest
from letter_n_gram_list import letter_n_gram_list
from inc_freq import inc_freq


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


if __name__ == "__main__":
    unittest.main()
