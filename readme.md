---
title: README
author: N_ha
---

サークルでの説明用に書き直したコードを上げます。

windowsを想定しています。

## 環境構築

1. Python 3.11 をインストール

   AtCoder に入っているのは `3.11.4` なので、 `3.11.x` を入れておけば基本的に問題ないはず

   [公式サイト](https://www.python.org/)

   [3.11.4 のリリースページ](https://www.python.org/downloads/release/python-3114/)

2. できたか確認

   以下のコマンドで `3.11.x` が返ってくるか

   ```powershell
   python -V
   ```

   Python ランチャーを使っている場合

   ```powershell
   py -V
   ```

3. 仮想環境の構築

   ```powershell
   python -m venv .venv
   .venv/Scripts/Activate.ps1
   ```

   venv じゃなくても大丈夫です。

4. AtCoder で利用できるライブラリのインストール

   [参考](https://docs.google.com/spreadsheets/d/1HXyOXt5bKwhKWXruzUvfMFHQtBxfZQ0047W7VVObnXI/edit#gid=408033513)

   `torch` は 1.13.1 の指定だが現在はインストール不可能なので適当なものをインストール(AtCoderだと基本使わないから入れなくても大丈夫だと思う)。

   ```powershell
   python -m pip install `
   numpy==1.24.1 `
   scipy==1.10.1 `
   networkx==3.0 `
   sympy==1.11.1 `
   sortedcontainers==2.4.0 `
   more-itertools==9.0.0 `
   shapely==2.0.0 `
   bitarray==2.6.2 `
   PuLP==2.7.0 `
   mpmath==1.2.1 `
   pandas==1.5.2 `
   z3-solver==4.12.1.0 `
   scikit-learn==1.2.0 `
   ortools==9.5.2237 `
   torch `
   polars==0.15.15 `
   lightgbm==3.3.1 `
   gmpy2==2.1.5 `
   numba==0.57.0 `
   git+https://github.com/not522/ac-library-python

   python -m pip install -U setuptools==66.0.0
   python -m pip install cppyy==2.4.1
   ```

   または

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. その他ライブラリのインストール

   ```powershell
   python -m pip install black isort
   ```

   * black: フォーマッター
   * isort: import の適正化

## 実行方法

普通に Python から実行できますが、 AtCoder 用に以下の機能をつけた `run.ps1` ファイルを作りました。

上記の環境構築を行い、 black 、 isort もインストールされていることが前提です。
また、実行前に仮想環境に入るのを忘れないでください。

### できること

* `create.ps1`
  * コンテストごとのフォルダを作成
  * 問題ごとのPythonファイルを `main.py` からコピー
* `run.ps1`
  * Python ファイルの実行
  * 入力ファイルと出力ファイルの受け取り
  * black と isort の実行

### 使い方

1. powershell を起動

   スタートボタン → 「powershell」で検索 などから起動できます。

2. 仮想環境に入る

   ```powershell
   .venv\Scripts\activate.ps1
   ```

3. コンテストフォルダの作成

   名前が `contest` のフォルダを作成し、その中に `problems` に含まれる問題ごとのPythonファイルを作成します。
   `problems` が空の場合フォルダ作成のみを行います。

   ```powershell
   .\create contest [-problems]
   ```

   例

   ```powershell
   .\create abc000 a,b,c,d,e
   ```

4. コーディング

   エディタでコーディングをしてください。
   VSCode がおすすめです。

5. 実行

  `in` のファイルを標準入力、 `out` のファイルを標準出力として `file` を実行します。

   ```powershell
   .\run file [-in .\in.txt] [-out .\out.txt]
   ```

   例

   ```powershell
   .\run main.py
   ```
