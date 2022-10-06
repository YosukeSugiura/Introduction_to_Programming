# Pythonの基本的な文法(3) : 繰り返し

---
## 練習問題
### 練習問題１： forループと要素の取り出し１

リスト内の要素は， `[ ]` と数字で取り出すことができます．
例えば，次のコードはリスト `Alphabet` の２番目の要素と４番目の要素を取り出して表示しています(０番目から数えてです)．
```Python
Alphabet = ['A', 'B', 'C', 'D', 'E']
print(List[2])	# C
print(List[4])	# E
```

それではこの性質を利用して `for` ループを作ってみましょう．
コード [`05_for_exercise.py`](05_for_exercise.py) を修正して，先ほどの [`05_for_check.py`](05_for_check.py) と同じ結果が出力されるようにしましょう．

ただし，コードにある `for` ループ
```Python
for k in range(4):
```
には手を加えないでください． `k` にはループを繰り返した回数(0からスタート)が入ります．

#### 解答

[>> `05_for_exercise_ans.py`](05_for_exercise_ans.py)



### 練習問題２： forループと要素の取り出し２

次のリスト内の要素をすべて足した結果を表示するコードを書きましょう．
`for` ループをうまく使ってください．

```Python
Numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34]
```

> ヒント： リスト `Numbers` の要素を１つずつ取り出し，足し合わせます．`for` ループの前にあらかじめ変数 `result = 0` を用意して，足し合わせた結果を代入していきましょう．

#### 解答

以下のように，`for` ループ内で `result` に取り出した要素を足し合わせていく．
```Python
result = 0
for num in Numbers:			# この行は修正しないでください．
	result = result + num
```

[>> `05_for_exercise_ans2.py`](05_for_exercise_ans2.py)

実行結果
```
88
```

--- 
[< 前へ](../04_if) | [トップに戻る](https://github.com/YosukeSugiura/Introduction_to_Programming) | [次へ >](../06_read_write) 
