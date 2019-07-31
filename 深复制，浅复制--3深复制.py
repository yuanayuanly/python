#深复制
import copy
a=[1,2,3,[4,5]]
b=copy.deepcopy(a)
print(id(a)==id(b))
print(id(a[0])==id(b[0]))
print(id(a[3][0])==id(b[3][0]))
#深复制相当于画两个没有交集的圆圈，分别贴上标签a和b，a与b的索引id不同，内部元素因为是刚复制过来的，所以id一样，更改元素值后会不同
a[0]=6
a[3][0]=7
print(id(a[0])==id(b[0]))
print(id(a[3][0])==id(b[3][0]))
#验证成功
