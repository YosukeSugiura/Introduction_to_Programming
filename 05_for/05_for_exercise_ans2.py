"""
リストを利用したforループ (リストの要素を指定する)
"""
Numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34]

# k には繰り返し回数が入る．
result = 0
for num in Numbers:			# この行は修正しないでください．
	result = result + num

print(result)