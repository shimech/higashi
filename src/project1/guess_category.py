import numpy as np

import sys
sys.path.append("./src/pre5")
from cos_sim import cos_sim


def guess_category(dv, v):
    cos_sim_dict = dict([[cate, cos_sim(np.array(x), np.array(v))]
                         for cate, x in dv.items()])
    return max(cos_sim_dict, key=cos_sim_dict.get)
