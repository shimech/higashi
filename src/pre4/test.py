import unittest
from ..utils import Utils
from replace_kutoten import replace_kutoten
from text_file_len import text_file_len


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


if __name__ == "__main__":
    unittest.main()
