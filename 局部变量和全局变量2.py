APPLE=100
a=None
def fun():
    global a
    a=20
    return a+100
print(APPLE)
#未运行定义函数之前的a的值
print('a past=',a)
print(fun())
#运行函数之后a的值
print('a now=',a)


