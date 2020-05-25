import unittest
from extract_frequent_words import extract_frequent_words


class TestExtractFrequentWords(unittest.TestCase):
    def test_extract_frequent_words(self):
        word_frequency = {"私": 2, "あなた": 4, "愛": 3, "別れ": 1}
        coverages = [0.0, 0.39, 0.69, 0.89, 0.99]
        expecteds = [
            [],
            ["あなた"],
            ["あなた", "愛"],
            ["あなた", "愛", "私"],
            ["あなた", "愛", "私", "別れ"]
        ]

        for coverage, expected in zip(coverages, expecteds):
            self.assertEqual(expected, extract_frequent_words(
                word_frequency, coverage))


if __name__ == "__main__":
    unittest.main()
