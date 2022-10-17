# モジュールと関数

---
## 練習問題
### 練習問題１： 関数の定義

コード [`07_module_ex1.py`](07_module_ex1.py) を眺めましょう．
ファイルからデータを読み込み，その読み込んだデータを別のファイルに書き込もうとしています．
関数 `write_file()` を正しく書き直し，データをファイルに書き出す処理を行うようにしてください．

> ヒント：関数 `write_file()` の引数の１つ目は書き出すデータ，引数の２つ目は書き出すファイル名です．

#### 解答

```Python
"""
	練習問題：関数の定義
"""
# 定義した関数を使う例
import pandas as pd
import numpy as np

# 関数：ファイルを読み込む
def read_file(file_name):
    input_data = pd.read_csv(file_name)
    input_data = np.array(input_data)
    return input_data

# 関数：ファイルを書き出す
# 	引数1：書き込むデータ，引数2：ファイル名
def write_file(data, output_file):
    # ファイルの書き込みを行う処理をここに書く
    df = pd.DataFrame(data)
    df.to_csv(output_file, header=False, index=False)
    return 0

# ファイルの読み込み
input_data1 = read_file('fruits.csv')
input_data2 = read_file('weather.csv')
input_data3 = read_file('icecream.csv')

# 読み込んだデータの表示
#print(input_data1)
#print(input_data2)
#print(input_data3)

# 書き込むファイルの名前
output_file1 = 'fruits_output.csv'
output_file2 = 'weather_output.csv'
output_file3 = 'icecream_output.csv'

# ファイルの書き込み
write_file(input_data1, output_file1)
write_file(input_data2, output_file2)
write_file(input_data3, output_file3)
```

---
## 演習課題
### 演習課題１： 関数の定義１

コード [`07_module_def.py`](07_module_def.py) を眺めましょう．第１の処理ではリストの中に指定した果物があるかを検索し，結果を表示します．第２の処理ではリストの中に指定した動物があるかを検索し，結果を表示します．これらの処理には共通する部分がありますよね．共通する処理を関数にしましょう．

> ヒント：関数を定義するとき，`検索するリスト`と`検索ワード`の２つを引数に設定しましょう．



---
[< 前へ](../06_read_write) | [トップに戻る](https://github.com/YosukeSugiura/Introduction_to_Programming) | 次へ > 
