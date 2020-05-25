import unittest
from min_sepal_width import min_sepal_width
from predict_titanic import predict_titanic


class TestMinSepalWidth(unittest.TestCase):
    def test_min_sepal_width(self):
        specieses = [
            "setosa",
            "versicolor",
            "virginica",
            "setosa",
            "versicolor",
            "virginica"
        ]
        sepal_lens = [
            5,
            5,
            5,
            5.8,
            5.8,
            5.8
        ]
        expecteds = [
            3.0,
            2.0,
            2.2,
            4.0,
            2.2,
            2.2
        ]

        for species, sepal_len, expected in zip(specieses, sepal_lens, expecteds):
            self.assertEqual(expected, min_sepal_width(species, sepal_len))


class TestPredictTitanic(unittest.TestCase):
    def test_predict_titanic(self):
        tsizes = [0.3, 0.2, 0.3, 0.2]
        rstates = [10, 10, 0, 0]
        expecteds = [73, 71, 70, 69]

        for tsize, rstate, expected in zip(tsizes, rstates, expecteds):
            self.assertEqual(expected, int(
                predict_titanic(tsize, rstate) * 100))


if __name__ == "__main__":
    unittest.main()
