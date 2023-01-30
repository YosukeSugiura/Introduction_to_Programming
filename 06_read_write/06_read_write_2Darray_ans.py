"""
	演習課題： ２次元データの取り扱い
"""
import pandas as pd
import numpy as np

# ファイルの読み込み
input_file = 'iris.csv'	# 読み込むファイル名
input_data = pd.read_csv(input_file)
input_data = np.array(input_data)

# 「variety」以外の要素を配列output_dataに入れる．．
output_data = []
for row in input_data:
	if row[4] == 'Setosa':
		output_data.append(row[0:2])
		
output_data = np.array(output_data) # おまじない

# ファイルの書き込み
output_file = 'output.csv'
df = pd.DataFrame(output_data)
df.to_csv(output_file, header=False, index=False)