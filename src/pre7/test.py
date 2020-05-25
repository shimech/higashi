import unittest
from min_sepal_width import min_sepal_width


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


if __name__ == "__main__":
    unittest.main()
