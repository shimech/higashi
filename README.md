# 東を救いたい

## 環境

- macOS Catalina 10.15.4
- Homebrew 2.2.13
- git 2.26.2
- pyenv 1.2.18
- Python 3.8.2
- pip 20.0.2
- pipenv 2018.11.26

## ソースコード一覧

| ディレクトリ | 問題                                                                                 | 文法                                                                                               |
| ------------ | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `ex1/`       | 1. 三角形の分類                                                                      | `if-else`                                                                                          |
| `pre2/`      | 1. リストの抜き出し<br> 2. 桁を増やす                                                | slice <br> 型の cast                                                                               |
| `ex2/`       | 1. ペアのリストから抜き出し                                                          | tuple?                                                                                             |
| `pre3/`      | 1. 文字列から文字 n-gram を生成する <br> 2. 文字列と辞書                             | `list.append()`? <br> `dict.get()`? (ゴミ関数)                                                     |
| `ex3/`       | 1. 行列の転置                                                                        | list 操作                                                                                          |
| `pre4/`      | 1. 全角文字を含む文字列の読み込みと書き出し <br> 2. ディレクトリ中のファイル読み込み | ファイル操作                                                                                       |
| `ex4/`       | 1. イテラブルの分割                                                                  | いろいろな`for` (ファイルの挙動は初めて知った)                                                     |
| `pre5/`      | 1. サイコロ <br> 2. コサイン類似度                                                   | 乱数 <br> `numpy`                                                                                  |
| `ex5/`       | 1. モジュールの作成                                                                  | 自作モジュールの作成と読込                                                                         |
| `pre6/`      | 1. 行列の最大要素とそのインデックス <br> 2. 最初の要素を除いたイテラブル             | 内包表記 <br> クラス、`__iter__()`                                                                 |
| `ex6/`       | 1. 頻出単語リストの作成                                                              | ?                                                                                                  |
| `pre7/`      | 1. pandas ライブラリ <br> 2. scikit-learn ライブラリ                                 | `pandas` <br> 機械学習！AI！                                                                       |
| `project1/`  | Wikipedia の自動分類をしよう                                                         | 各カテゴリの頻出単語から生成されたベクトルを参照し、コサイン類似度を用いて記事をカテゴライズする。 |
| `project2/`  | 自分のアイディアで手法を改良しよう                                                   | `project1`の課題を、手法を変えて高精度化する。                                                     |

## コマンド一覧

### パッケージのインストール

```shell
$ pipenv install
```

### テストの実行

```shell
$ pipenv run test {DIRNAMES}
```

※ `DIRNAMES` を指定せずに実行すると、すべてのテストを実行する。

### Jupyter Notebook の起動

```shell
$ pipenv run jupyter notebook
```

## インストール手順

```shell
$ command
```

と書かれた箇所は、`ターミナル.app`に打ち込む。

### 1. Xcode のインストール

[ここ](https://apps.apple.com/jp/app/xcode/id497799835?mt=12&ign-mpt=uo%3D4)から App Store 経由でインストール

```shell
$ xcode-select --install
```

### 2. Homebrew のインストール

```shell
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
$ brew --version
Homebrew 2.2.13
Homebrew/homebrew-core (git revision fb0aa; last commit 2020-04-26)
Homebrew/homebrew-cask (git revision 6aa1b; last commit 2020-04-26)
```

### 3. git のインストール

```shell
$ brew install git
$ git --version
git version 2.26.2
```

### 4. pyenv のインストール

```shell
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ source ~/.bashrc
$ pyenv --version
pyenv 1.2.18
```

### 5. Python のインストール

```shell
$ pyenv install 3.8.2
$ pyenv rehash
$ pyenv global 3.8.2
$ pyenv versions
  system
* 3.8.2 (set by /Users/{USER_NAME}/.pyenv/version)
$ python --version
Python 3.8.2
```

### 6. pipenv のインストール

```shell
$ pip install --upgrade pip
$ pip --version
pip 20.0.2 from /Users/{USER_NAME}/.pyenv/versions/3.8.2/lib/python3.8/site-packages/pip (python 3.8)
$ pip install pipenv
$ pipenv --version
pipenv, version 2018.11.26
```

### 7. リポジトリのクローン、パッケージのインストール

※ `cd` で好きな場所に移動してから、

```shell
$ git clone https://github.com/shimech/higashi.git
$ cd higashi
$ pipenv install
Installing dependencies from Pipfile.lock (236ab5)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 2/2 — 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

### 8. テストの実行

```shell
$ pwd
{なんでもいい}/higashi
$ git pull origin master
$ pipenv run test
test_between (__main__.TestBetween) ... ok
test_classify_triangle (__main__.TestClassifyTriangle) ... ok

(省略)

----------------------------------------------------------------------
Ran 7 tests in 0.002s

OK
```

最後の行が `OK` であればテスト通過、`FAILED` であれば間違っている。
