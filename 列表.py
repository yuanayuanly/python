#1定义 索引 添加 删除 修改
list=['我爱','鲸鱼','吃虾']#一定记得要用逗号分隔开
#2索引
print(list[1])
#3添加，append()方法
list.append('爱我')
print(list)
#4删除： remove和pop方法
list.pop(0)#移除指定位置元素
print(list)
list.remove('鲸鱼')
print(list)
#5修改（replace是针对字符串的替换），列表替换用下面方式
list[0]='北京'
print(list)
'''
列表的其他操作：
list.count(obj) 统计某个元素在列表中出现的次数
list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj) 将对象插入列表
list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj) 移除列表中某个值的第一个匹配项
list.reverse() 反向列表中元素
list.sort(cmp=None, key=None, reverse=False) 对原列表进行排序
'''
ab=list.count('北京')
print(ab)
list.reverse()
print(list)
