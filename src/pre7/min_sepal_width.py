import os
import pandas as pd


def min_sepal_width(species, sepal_len):
    csvpath = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "csv/iris.csv")  # 環境に合わせて変更する
    df = pd.read_csv(csvpath)
    return df.query("species == '{}' and sepal_length >= {}".format(species, sepal_len))["sepal_width"].min()
