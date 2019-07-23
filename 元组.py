'''Python的元组与列表类似，不同之处在于元组的元素不能修改，一般用小括号(“()”) 包裹。
例如：tuple1 = (1, 2, 3)。 在例子中，tuple1为变量名，(1, 2, 3)为元组。'''
#1:索引
tuple1=(1,2,3)
print(tuple1[0])
#2：不可修改
#tuple1[0] = 6  #报错：'tuple' object does not support item assignmentb
'''
len(tuple) 计算元组元素个数。
max(tuple) 返回元组中元素最大值。
min(tuple) 返回元组中元素最小值。
tuple(seq) 将列表转换为元组。'''
#3:
print(len(tuple1))
aaa=[3,2,1]
print(tuple(aaa))
