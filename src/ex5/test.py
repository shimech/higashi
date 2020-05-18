import unittest
import mymodule


class TestMycsvread(unittest.TestCase):
    def test_mycsvread(self):
        csvfiles = ["./src/ex5/csv/small.csv"]
        codes = ["sjis"]
        expecteds = [[["11", "12", "13", "14", "15"], [
            "21", "22", "23", "24", "25"], ["31", "32", "33", "34", "35"]]]

        for csvfile, code, expected in zip(csvfiles, codes, expecteds):
            self.assertEqual(expected, mymodule.mycsvread(csvfile, code))


if __name__ == "__main__":
    unittest.main()
