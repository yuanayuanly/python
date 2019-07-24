jihe={'apple','orange','flowers','flowers','apple'}
#1：去重功能
print(jihe)
#2:判断元素是否在集合内
print('orange' in jihe)#元素必须加上引号才能判断哦
#3:集合之间的运算
#多个单字母元素集合的快速设定方法
a = set('abracadabra')
b = set('alacazam')
#下面部分画圆圈图讲解：
print(a)# 集合a中包含而集合b中不包含的元素
print(a|b)# 集合a或b中包含的所有元素
print(a&b) # 集合a和b中都包含了的元素a
print(a^b)# 不同时包含于a和b的元素
#4：类似列表推导式，同样集合支持集合推导式
c={x for x in a if x not in 'abc'}
print(c)#上面两行代码不能合并写成print{x.....},不过变量c也可以写成a与原集合重名，但注意这样会替换集合a中的元素
#5：集合添加元素
jihe.add('girl')
print(jihe)
#用update添加，参数可以是元素，列表，元组，字典等
jihe.update({1,3})
print(jihe)
#update元素可以有多个，用逗号分开
jihe.update({6,7},{4,5})
print(jihe)
#6:移除元素：（1）集合名.remove,此方法需要注意若元素不存在，会发生错误(2)集合名.discard，此方法即使元素不存在也不会发生错误
#7：随机删除集合中的一个元素
jihe2={'red','yellow','blue'}
print(jihe2.pop())#此行是先从集合中随机选出一个元素
print(jihe2)#此行将上面所选元素删除掉
#8：计算集合中元素个数
print(len(jihe2))
#9:清空集合
print(jihe2.clear())#或者分两行写：jihe2.clear()   print(jihe2)
#10:判断元素是否在集合中
print('apple'in jihe)



