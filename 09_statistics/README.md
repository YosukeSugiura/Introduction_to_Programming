# 統計と線形回帰

---
## 授業のポイント

- 演習の時間では「大数の法則や「中心極限定理」，「最尤推定」は完全に割愛する．
- 演習問題の[`09_polynomial_regression2.py`](09_polynomial_regression2.py)は，こっそりとデータを **標準化** してる．
  - 標準化の意味と計算方法は…説明するか迷って割愛した．
  - 練習課題のコードではデータを標準化していない．
- 演習課題の採点には，下記の観点から行っていた．
  - データに対するアプローチを説明できているか．
  - 結果を明示できているか．
  - 結果に対する考察を論理的に展開できているか．


---
## 練習問題
### 練習問題１：線形回帰と多項式回帰

コード [`09_linear_regression.py`](09_linear_regression.py) を実行し，線形回帰を適用したときのみかん収穫量の予測結果を確認せよ．
またコード [`09_polynomial_regression.py`](09_polynomial_regression.py)を実行し，多項式回帰を適用したときのみかん収穫量の予測結果を確認せよ．

データは次のURLからダウンロードしてください．  
[>> `fruits.csv`](https://raw.githubusercontent.com/YosukeSugiura/Introduction_to_Programming/main/09_statistics/fruits.csv)

### 練習問題２：多項式回帰の次数と過学習

コード [`09_polynomial_regression.py`](09_polynomial_regression.py)の多項式次数(degree)を増加させたときに，
R2スコアがどう変化するか，そして2023年，2030年の収穫量の予測結果がどう変化するかを確認せよ．

---
## 演習課題
### 演習課題１：様々な回帰モデル

コード [`09_polynomial_regression2.py`](09_polynomial_regression2.py)を見てみましょう．
このコードは1946年～2020年の消費者物価指数のデータ([`bukka.csv`](https://raw.githubusercontent.com/YosukeSugiura/Introduction_to_Programming/main/09_statistics/bukka.csv))に対して多項式回帰を適用したものです．

データは次のURLからダウンロードしてください．  
[>> `bukka.csv`](https://raw.githubusercontent.com/YosukeSugiura/Introduction_to_Programming/main/09_statistics/bukka.csv)

このデータには，0列目に年次が，1列目に消費者物価指数が入っています．

コードを修正し，多項式次数(degree)を変更したり，様々なモデルを利用して回帰を行ってみましょう．
R2スコアや2023年，2030年の予測消費者物価指数はどのように変化するでしょうか？
下に，回帰モデルの例を示します．自身で調べてみて，活用してみましょう．

- 線形回帰
- 多項式回帰
- リッジ回帰 (`sklearn.linear_model.Ridge()`)
- ラッソ回帰 (`sklearn.linear_model.Lasso()`)

#### 解答

解答の参考まで．  
[>> 消費者物価指数のモデリング.ipynb](消費者物価指数のモデリング.ipynb)

---
[< 前へ](../08_prob_plot) | [トップに戻る](https://github.com/YosukeSugiura/Introduction_to_Programming/tree/minor) | 
