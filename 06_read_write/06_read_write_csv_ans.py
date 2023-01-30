"""
	練習課題： csvファイルの読み書き
"""
import pandas as pd
import numpy as np

# ファイルの読み込み
input_file = 'iris.csv'	# 読み込むファイル名
input_data = pd.read_csv(input_file)
input_data = np.array(input_data)

print(input_data[:,4])