import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def predict_titanic(tsize, rstate):
    csvpath = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "csv/titanic.csv")  # 環境に合わせて変更する
    df = pd.read_csv(csvpath)
    X = df[["Pclass", "Fare", "Age"]]
    y = df["Survived"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=tsize, random_state=rstate, stratify=y)

    lr = LogisticRegression().fit(X_train, y_train)
    return accuracy_score(lr.predict(X_test), y_test)
