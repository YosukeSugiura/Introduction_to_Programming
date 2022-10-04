"""
	練習課題： csvファイルの読み書き
"""

# 先頭行を読み込む
import numpy as np

input_file = 'iris.csv'	# 読み込むファイル名
input_data = np.loadtxt(input_file, delimiter=',', skiprows=0)

print(input_data)