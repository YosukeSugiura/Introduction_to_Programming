"""
リストを利用したforループ (リストの要素を指定する)
"""
Numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34]

result = 0
for num in Numbers: # num には Numbers の要素が１つづつ出される．
	result = result + num

print(result)
