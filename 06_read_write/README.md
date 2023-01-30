# Pythonを使ったファイルの読み書き

---
## 授業のポイント

- ファイルの保存のやり方は，
1. リンクを右クリック．
2. 「リンク先のファイルを保存」を選択．
3. 保存名を「○○.txt」から「○○.csv」と変更する．
4. 保存．

- Google Colaboratory へのアップロードするには，ファイルフォルダーに保存したファイルをドラッグ&ドロップ．Google Driveにマウントする必要はない．

---
## 練習問題
### 練習問題１： ファイルの読み込み

コード [`06_read_write_csv.py`](06_read_write_csv.py) を実行しましょう．

実行前に，まずは保存した [`iris.csv`](iris.csv) を Colaboratory のワークスペースに置きます．(自身のPCにファイルを保存するにはブラウザの `右クリック → 名前をつけて保存` からできます．)

##### Colaboratory のワークスペースへのデータの設置
1. Colaboratory 画面左の 「フォルダアイコン」 をクリックする．
2. 出てくるファイルウィンドウに [`iris.csv`](iris.csv) をドラッグ&ドロップで設置する．

実行すると，データの中身を見ることができます．

#### 解答

なし.

### 練習問題２： 列の取り出し

コード [`06_read_write_csv.py`](06_read_write_csv.py) を修正して，[`iris.csv`](iris.csv) の「variety」に対応する列の値のみを表示させましょう．どのような種があるでしょうか？

#### 解答

[>> `06_read_write_csv_ans.py`](06_read_write_csv_ans.py)

---
## 演習課題
### 演習課題１：特定の文字列に一致する行の取り出し

コード [`06_read_write_2Darray.py`](06_read_write_2Darray.py) は「variety」に対応する列以外の列の値を全て取り出し，新たな配列 `output_data` に入れています．実行して確認しましょう．

このコードを修正し，「variety」が `Setosa` となる行の，がく片の長さと幅をすべて取り出しましょう.
さらに，その取り出したデータを `output.csv` ファイルに保存しましょう．

> ヒント： 繰り返し処理で学んだように， `if` 文を使って「variety」の列の値が `Setosa` の行のみを取り出します．

#### 解答

[>> `06_read_write_2Darray_ans.py`](06_read_write_2Darray_ans.py)

--- 
[< 前へ](../05_for) | [トップに戻る](https://github.com/YosukeSugiura/Introduction_to_Programming/tree/minor) | [次へ >](../07_module)
