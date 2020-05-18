import unittest
from split_iterable import split_iterable

import sys
sys.path.append("./src")


class TestSplitIterable(unittest.TestCase):
    def setUp(self):
        import os
        from utils import Utils

        self.dirname = Utils.make_dir("./tmp")

        self.filename = os.path.join(self.dirname, "gokigenyou.txt")
        with open(self.filename, mode="w", encoding="utf-8") as f:
            f.write("こんにちは。\nごきげんよう。\n\nさようなら。\n")

    def tearDown(self):
        from utils import Utils

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


if __name__ == "__main__":
    unittest.main()
