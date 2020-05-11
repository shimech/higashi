import numpy as np


def cos_sim(x, y):
    return np.sum(x * y) / (np.sqrt(np.sum(x * x)) * np.sqrt(np.sum(y * y)))
