# 3. Pythonの基本的な文法(1) : 表示

---
## 練習問題
### 練習問題１： printの使い方

コード [`03_print_exercise.py`](03_print_exercise.py) を見てみましょう．このコードの最後に追加して，実行結果に「xとyの和は〇です．xとzの積は△です．」と表示させてみましょう．  
ここで〇と△には，それぞれの計算結果を表示するようにしてください．  

> ヒント： ここでは print(' ... '.format()) 構文を利用しましょう．

#### 解答

[>>`03_print_exercise_ans1.py`](03_print_exercise_ans1.py)

```
xとyの和は30です．xとzの積は20です．
```


### 練習問題２： 文字列の演算

Pythonでは文字列に対して足し算・掛け算ができます．それを確認します．

練習問題１で書いたコードをコピーして保存します．
そしてそのコードの５行目と６行目を書き直し，`x` に `Pine` という文字を，`y` に `Apple` という文字を代入しましょう．
実行した場合，どのような結果が出てくるでしょうか？

#### 解答

- 文字列の足し算：文字列を結合する．  
'Pine' + 'Apple' → 'PineApple'  
- 文字列に正の整数をかけ算：文字列を数値の数だけ並べる．  
'Pine' * 2 → 'PinePine' 

[>>`03_print_exercise_ans2.py`](03_print_exercise_ans2.py)

```
xとyの和はPineAppleです．xとzの積はPinePineです．
```

--- 
[< 前へ](../02_Environment) | [トップに戻る](https://github.com/YosukeSugiura/Introduction_to_Programming) | [次へ >](../04_if) 
