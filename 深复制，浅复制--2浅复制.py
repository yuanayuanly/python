#浅复制：(深复制和浅复制都为自带模块，使用前需先import)
#1：
'''
import copy
a=[1,2,3]
b=copy.copy(a)
print(a)
print(b)
print(id(a))
print(id(b))
#运行后可以发现，a,b的元素值都相同，但是位置id不同，相当于有两个圆圈，分别贴上标签a和b，a圈中元素复制一遍放到b中
print(id(a[0]))
print(id(b[0]))
#因为元素是复制过去的，此时的元素的位置id相同
a[0]=444
print(a)
print(b)
#与赋值不同，因为此时储存在两个不同圆圈中，a与b的位置id不同，所以，改变一个标签下的元素值，另一个标签下同位置的元素不会变化
print(id(a[0]))
print(id(b[0]))
#此时我们发现a,b标签下第一个位置元素的索引id不相同啦
'''

#2:
import copy
a=[1,2,3,[4,5]]
b=copy.copy(a)
print(a)
print(b)
#运行结果可以看到内嵌列表也会被复制到另一个标签下的圆圈下
'''运行结果中分别输入id(a)==id(b),id(a[3][0])==id(b[3][0]),可以发现第一个指令返回错误，第二个指令返回正确，
说明浅复制相当于两个有交叉部分的圆圈，而内嵌列表正好处于交叉位置下，此位置下元素的索引id相同，所以可以推测，
改变任一标签下该位置元素，另一标签下该位置元素也应该会跟随变化'''
#验证
b[3][0]=666
print(a)
print(b)
print(id(a[3][0])==id(b[3][0]))
