---
title: readme
author: N_ha
---

## 環境構築

windowsを想定

1. Python 3.11 をインストール

   [公式サイト](https://www.python.org/downloads/)

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

4. ライブラリのインストール

   [参考](https://docs.google.com/spreadsheets/d/1HXyOXt5bKwhKWXruzUvfMFHQtBxfZQ0047W7VVObnXI/edit#gid=408033513)

   `torch` は 1.13.1 の指定だが現在はインストール不可能なので適当なものをインストール

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
