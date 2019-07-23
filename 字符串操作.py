'''
字符串操作
连接: "+"
重复输出： "*"
替换： replace(旧文本, 新文本)
分隔： split(分隔符)
字符串索引
#连接和重复
成员运算符
'''
name1='我爱'
name2='鲸鱼编程'
print(name1+name2)
print(name2*3)

#2替换
# 代码用法str.rep#lace(old, new)
aaa='我爱小鲸鱼'
bbb=aaa.replace('爱','喜欢')#注意逗号一定是要在英文输入法下打出的
print(bbb)

#分隔
# 代码用法 str.split(str, num)
# str:分隔字符串样式，默认为空格  num:分隔次数，默认为-1,即全部
ccc='我 爱 小鲸鱼'
ddd=ccc.split(" ")#注意引号之间一定要有空格
print(ddd)
#字符串索引
fff='我爱小鲸鱼'
print(fff[0])
#成员运算符：
'''符号：in
定义如果在指定的序列中找到值返回 True，否则返回 False。

符号：not in
定义如果在指定的序列中没有找到值返回 True，否则返回 False。'''
string = "我爱鲸鱼"
print("鲸鱼" in string)
print('鲸鱼' in string)
