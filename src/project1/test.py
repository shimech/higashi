import unittest
from str2words import str2words
from compute_word_frequency import compute_word_frequency
from words2vec import words2vec
from guess_category import guess_category


class TestStr2words(unittest.TestCase):
    def test_str2words(self):
        A = {}
        with open("./src/project1/csv/Articles.csv", mode="r", encoding="utf-8") as f:
            next(f)
            for line in f:
                line = line.replace("\\n", "\n")
                title, text = line.split("\t")
                A[title] = text

        docs = [
            A["寄生バチ"],
            A["東京アニメセンター"]
        ]
        indices = [
            [0, 14],
            [120, 130]
        ]
        expecteds = [
            ["寄生", "バチ", "寄生", "バチ", "きせる", "バチ", "やどる",
                "バチ", "寄生", "蜂", "ハチ", "目", "うち", "生活"],
            ["映画", "祭", "行う", "施設", "2017", "年", "移転", "後", "UDX", "シアター"]
        ]

        for doc, index, expected in zip(docs, indices, expecteds):
            self.assertEqual(expected, str2words(doc)[index[0]:index[1]])


class TestComputeWordFrequency(unittest.TestCase):
    def test_compute_word_frequency(self):
        Dw = {}
        for cate in ("animal", "art", "economy", "law", "plant", "politics"):
            Dw[cate] = []
        with open("./src/project1/csv/wiki_dataset.csv", mode="r", encoding="utf-8") as f:
            next(f)
            for line in f:
                cate, title, words = line.replace("\\n", "\n").split("\t")
                Dw[cate].extend(words.split(" "))

        dic = compute_word_frequency(Dw)

        values = [len(dic), sum(dic.values())]
        expecteds = [59870, 1164533]

        for value, expected in zip(values, expecteds):
            self.assertEqual(value, expected)


class TestWords2vec(unittest.TestCase):
    def test_words2vec(self):
        words_list = [
            ["a", "b", "c", "d", "f", "a", "a", "a", "b", "d", "d"],
            ["今日", "雨", "明日", "雨", "明後日", "曇り"]
        ]
        frequent_words_list = [
            ["a", "b", "c", "d", "e"],
            ["晴れ", "曇り", "雨"]
        ]
        expecteds = [
            [4, 2, 1, 3, 0],
            [0, 1, 2]
        ]

        for words, frequent_words, expected in zip(words_list, frequent_words_list, expecteds):
            self.assertEqual(expected, words2vec(words, frequent_words))


class TestGuessCategory(unittest.TestCase):
    def test_guess_category(self):
        import sys

        A = {}
        with open("./src/project1/csv/Articles.csv", mode="r", encoding="utf-8") as f:
            next(f)
            for line in f:
                line = line.replace("\\n", "\n")
                title, text = line.split("\t")
                A[title] = text

        Aw = {}
        for title, text in A.items():
            Aw[title] = str2words(text)

        Dw = {}
        for cate in ("animal", "art", "economy", "law", "plant", "politics"):
            Dw[cate] = []
        with open("./src/project1/csv/wiki_dataset.csv", mode="r", encoding="utf-8") as f:
            next(f)
            for line in f:
                cate, title, words = line.replace("\\n", "\n").split("\t")
                Dw[cate].extend(words.split(" "))

        W = compute_word_frequency(Dw)

        sys.path.append("./src/ex6")
        from extract_frequent_words import extract_frequent_words
        F = extract_frequent_words(W, 0.5)

        Av = {}
        for title, words in Aw.items():
            Av[title] = words2vec(words, F)

        Dv = {}
        for cate, words in Dw.items():
            Dv[cate] = words2vec(words, F)

        vs = [
            Av["寄生バチ"],
            Av["東京アニメセンター"],
            Av["キャッシュ・フロー"],
            Av["請求権と自由権"],
            Av["グネモン"],
            Av["ドクトリン"]
        ]
        expecteds = [
            "animal",
            "art",
            "economy",
            "law",
            "plant",
            "politics"
        ]

        for v, expected in zip(vs, expecteds):
            self.assertEqual(expected, guess_category(Dv, v))


if __name__ == "__main__":
    unittest.main()
