import unittest
from utils import Utils
from ex1.classify_triangle import classify_triangle
from pre2.between import between
from pre2.inc_digits import inc_digits
from ex2.tuple_list import tuple_list
from pre3.letter_n_gram_list import letter_n_gram_list
from pre3.inc_freq import inc_freq
from ex3.transpose import transpose
from pre4.replace_kutoten import replace_kutoten
from pre4.text_file_len import text_file_len
from ex4.split_iterable import split_iterable
from pre5.dice import dice
from pre5.cos_sim import cos_sim


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


class TestReplaceKutoten(unittest.TestCase):
    def setUp(self):
        self.dirname = Utils.make_dir("./tmp")

    def tearDown(self):
        Utils.remove_dir(self.dirname)

    def test_replace_kutoten(self):
        import os

        filenames = [
            "konnichiha.txt",
        ]
        codes = [
            "utf-8",
        ]
        texts = [
            "こんにちは、元気ですか。\nさようなら。\n",
        ]
        new_filenames = [
            "new-konnichiha.txt",
        ]
        expecteds = [
            "こんにちは，元気ですか．\nさようなら．\n",
        ]

        for filename, code, text, new_filename, expected in zip(filenames, codes, texts, new_filenames, expecteds):
            filename = os.path.join(self.dirname, filename)
            new_filename = os.path.join(self.dirname, new_filename)

            if os.path.exists(filename):
                os.remove(filename)
            if os.path.exists(new_filename):
                os.remove(new_filename)

            with open(filename, mode="w", encoding=code) as f:
                f.write(text)

            replace_kutoten(filename, code)

            with open(new_filename, mode="r", encoding=code) as f:
                self.assertEqual(expected, f.read())


class TestTextFileLen(unittest.TestCase):
    def test_text_file_len(self):
        import os
        path = "./src/pre4/txt"

        filenames = [
            "short.txt",
            "novel.txt",
            "preamble.md",
        ]
        codes = [
            "utf-8",
            "utf-8",
            "euc-jp"
        ]
        expecteds = [
            5,
            234,
            663
        ]

        for filename, code, expected in zip(filenames, codes, expecteds):
            filename = os.path.join(path, filename)
            self.assertEqual(expected, text_file_len(filename, code))


class TestSplitIterable(unittest.TestCase):
    def setUp(self):
        import os
        self.dirname = Utils.make_dir("./tmp")

        self.filename = os.path.join(self.dirname, "gokigenyou.txt")
        with open(self.filename, mode="w", encoding="utf-8") as f:
            f.write("こんにちは。\nごきげんよう。\n\nさようなら。\n")

    def tearDown(self):
        self.f.close()
        Utils.remove_dir(self.dirname)

    def test_split_iterable(self):
        self.f = open(self.filename, mode="r", encoding="utf-8")
        xss = [
            [1, 2, 0, 3, 4, 5, 0],
            [],
            self.f
        ]
        ys = [
            0,
            0,
            "\n"
        ]
        expecteds = [
            [[1, 2], [3, 4, 5], []],
            [[]],
            [["こんにちは。\n", "ごきげんよう。\n"], ["さようなら。\n"]]
        ]

        for xs, y, expected in zip(xss, ys, expecteds):
            self.assertEqual(expected, split_iterable(xs, y))


class TestDice(unittest.TestCase):
    def test_dice(self):
        args = [98, 112]
        expecteds = [(3, 5), (4, 6)]

        for arg, expected in zip(args, expecteds):
            self.assertEqual(expected, dice(arg))


class TestCosSim(unittest.TestCase):
    def test_cos_sim(self):
        import numpy as np
        import scipy.spatial.distance

        def gen_testcase(n):
            np.random.seed(0)
            x = np.random.rand(n)
            y = np.random.rand(n)
            ans = 1 - scipy.spatial.distance.cosine(x, y)
            return x, y, ans

        n_test = 3
        for i in range(n_test):
            np.random.seed(0)
            x, y, expected = gen_testcase(10**i)
            self.assertLess(abs(expected - cos_sim(x, y)), 1e-10)


if __name__ == "__main__":
    unittest.main()
