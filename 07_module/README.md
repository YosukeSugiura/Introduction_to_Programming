# モジュールと関数

Pythonは他のプログラミング言語と比べて，短いコードで複雑な処理を実行できるという特徴があります．
それを実現している要因が「モジュールと関数」が豊富に用意してあることです．
ここでは，モジュールと関数の使い方について学びましょう．

--- 
### モジュールと関数

前の章のコードをもう一度見てみましょう．
```Python
# ヘッダーあり
import pandas as pd
import numpy as np
 
input_file = 'input.csv'	# 読み込むファイル名
input_data = pd.read_csv(input_file)
input_data = np.array(input_data)
```


---
[< 前へ](../06_read_write) | [トップに戻る](../) | 次へ > 