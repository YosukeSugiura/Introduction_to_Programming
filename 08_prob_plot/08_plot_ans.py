import numpy as np  # Numpyモジュール
import pandas as pd # Pandasモジュール
import scipy as sp  # 数値計算用モジュール
import matplotlib.pyplot as plt   # プロット用モジュール
import japanize_matplotlib # 日本語表示用モジュール


"""
データの読みこみ
"""
input_file = 'score_A.csv'  # 読み込むファイル名
input_data = pd.read_csv(input_file)
input_data = np.array(input_data)

id = input_data[:,0] # 学籍番号
score = input_data[:,1] # テストの点数

# 点のプロット
plt.figure()
plt.plot(id,score,'.')
plt.xlabel('ID')
plt.ylabel('点数')

# 折れ線グラフ
plt.figure()
plt.plot(id,score)
plt.xlabel('ID')
plt.ylabel('点数')

# 棒グラフ
plt.figure()
plt.bar(id,score)
plt.xlabel('ID')
plt.ylabel('点数')