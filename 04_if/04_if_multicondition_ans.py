"""
演習課題４．３：複数の条件を用いた分岐
"""

x_name = 'Apple'
y_name = 'Orange'
z_name = 'Banana'

print('x, y, z はそれぞれ{0},{1},{2}である．'.format(x_name, y_name, z_name))

# ここに条件分岐を書いて，次の文章のいずれかを表示させたい．
if x_name=='Apple' or y_name=='Apple' or z_name=='Apple':
    if x_name=='Kiwi' or y_name=='Kiwi' or z_name=='Kiwi' :
        print('この中にリンゴとキウイはある．')
    else:
        print('この中にリンゴはあり，キウイはない．')
elif x_name=='Kiwi' or y_name=='Kiwi' or z_name=='Kiwi' :
    print('この中にリンゴはなく，キウイはある．')
else:
    print('この中にリンゴもキウイもない．')