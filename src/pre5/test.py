import unittest
from dice import dice
from com_sim import com_sim


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
