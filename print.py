#用法1：
#print(1)

#2
'''print 一句话注意加引号，单双号邪恶选择要看与句子中的符号有无冲突
print("we're going to do something")'''

#3
'''下句中引号冲突，反馈就会报错。
print('we're going to do something')
加引号会变彩色，说明想要计算机输出的为字符串，原色显示的为变量名或其他指令'''

#4
'''有冲突，但又只想用一种符号的方法：
print('I\'m jingyu')'''
#print('apple'+'car')

#5
'''
#字符串和数字是两种不同的数据类型，不能合并一起打印输出
#print('apple'+4)
#解决办法：把数字变为字符串
print('apple'+'4')
#或者也可以这样写
print('apple'+str(4))
'''

#6
#打印数字和打印算式
'''print(1+2)
print('1'+'2')
print('1+2')
'''

#7
#字符串转数字（分为整数型和小数型（又称浮点型））
print(int('1')+2)
print(float('1.2')+2)
