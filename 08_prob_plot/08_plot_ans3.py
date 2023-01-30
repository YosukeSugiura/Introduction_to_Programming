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

# 平均
mean = np.mean(score)
# 分散
var = np.var(score)
# 標準偏差
std = np.std(score)
# 中央値
med = np.median(score)

# 最頻値
uniq, freq = np.unique(score, return_counts=True) # uniq : リストの値，freq : 各出現回数，が得られる
mode = uniq[np.argmax(freq)] # freq から最も出現回数の大きい値を抜き出す．mode : 最頻値

print('Score_A')
print('Mean:{0}'.format(mean))
print('Variance:{0}'.format(var))
print('Standard Deviation:{0}'.format(std))
print('Median:{0}'.format(med))
print('Mode:{0}'.format(mode))

"""
データの読みこみ
"""
input_file = 'score_B.csv'  # 読み込むファイル名
input_data = pd.read_csv(input_file)
input_data = np.array(input_data)

id = input_data[:,0] # 学籍番号
score = input_data[:,1] # テストの点数

# 平均
mean = np.mean(score)
# 分散
var = np.var(score)
# 標準偏差
std = np.std(score)
# 中央値
med = np.median(score)

# 最頻値
uniq, freq = np.unique(score, return_counts=True) # uniq : リストの値，freq : 各出現回数，が得られる
mode = uniq[np.argmax(freq)] # freq から最も出現回数の大きい値を抜き出す．mode : 最頻値

print('\nScore_B')
print('Mean:{0}'.format(mean))
print('Variance:{0}'.format(var))
print('Standard Deviation:{0}'.format(std))
print('Median:{0}'.format(med))
print('Mode:{0}'.format(mode))