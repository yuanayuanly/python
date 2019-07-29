# 在这里写上你的代码 :-)
def function():
    print('this is a function')
    a=1+2
    print(a)
#上面的代码点击运行不会有反应，在运行结果中或者下面函数之外输入function（）即可看到结果。
function()

#2：
'''
def my_print(str1):
    print(str1+'我爱鲸鱼')
my_print('告诉你哦，')


#3：传递参数
#这里展示了两种传入参数的方式
my_print('鲸鱼AI')    #普通参数
my_print(str1 ='鲸鱼AI')  #关键字参数

def my_print_2(str1,str2):  #这个函数有两个传入参数，并将其合并输出
    print(str1+str2)

#4：给参数定义默认值，在没有参数传入的时候会调用默认值。
def my_print_3(str1='我爱鲸鱼'):  #这个函数有两个传入参数，并将其合并输出
    print(str1)
my_print_3()  
my_print_3('I love Dayu')

#5:传入参数的个数还可以发生变化
def my_print4(*str):
    for i in str:
        print(i)
    return 
my_print4('波妞','喜欢','宗介')

list=('boniu','like','zongjie')
my_print4(*list)#尝试去掉*的效果时怎样的
'''
#6：函数返回值
#return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
def sum(value1,value2):
    total=value1+value2
    return total
print(sum(200,300))
'''
上面代码也可以写成：
def sum(value1,value2):
    print(value1+value2)
sum(200,300)
'''
#7：内嵌函数和闭包,内嵌函数调用局部变量(下面代码容易出错，多独立练习几遍)
def fun():
    string1='鲸鱼'
    def foo(string2):
        print(string1+string2)
    foo('AI')
fun()

