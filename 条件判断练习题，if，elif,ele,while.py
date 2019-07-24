'''#1：小狗年龄判断
age=int(input('请输入你家小狗的年龄 '))#int定义输入必须为整型，若有小数则会报错
print('')
#上面程序可以改写成：print(int((input('请输入你家小狗的年龄 '))))
if age<0:
    print('你怕不是在逗我吧')
#注意赋值符号=与等于号==的区别
elif age==1:
    print('你家狗狗14岁了哦')
elif age==2:
    print('你家狗狗22岁了哦')
elif age>2:
    age2=22+(age-2)*5
    print('你家狗狗%d岁了哦' %age2)
    #2：数值判断（elif:否则如果，是否则如果，不是否则或者如果哦）
print(5==6)
#3:数字猜谜游戏：
#讲解思路，先不设定num2和while语句，分析后添加while语句，运行报错后再添加num2
num1=7
num2=-1#num2初始值可为不等于num1的任意值
print('欢迎进入猜数字游戏')
while num2!=num1:#若无while语句，则循环只判断一次就结束了
    num2=int(input('请输入猜的数字 '))
    if num2==num1:
        print('恭喜你答对了哦')
    elif num2<num1:
        print('猜的数字有点小哦')
    elif num2>num1:
        print('猜的数字有点大哦')
#4:判断数字能否整除2和3(注意：（1）if语句和elde语句之后都要加冒号（2）=与==的区别)
#注意观察else与elif的区别
num3=int(input('请输入一个数字 '))
if num3%2==0:
    if num3%3==0:
        print('你输入的数字可以整除2和3')
    else:
        print('你输入的数字可以整除2，但不能整除3')
else:
    if num3%3==0:
        print('你输入的数字可以被3整除，但不能被2整除')
    else:
        print('你输入的数字不能被2整除也不能被3整除')
'''

'''
#5:用if与elif的组合形式方法如下：（注意：elif内部不能嵌套else）
num3=int(input('请输入一个数字 '))
if num3%2==0:
    if num3%3==0:
        print('你输入的数字可以整除2和3')
    else:
        print('你输入的数字可以整除2，但不能整除3')
elif num3%3==0:
    print('你输入的数字可以整除3，但是不能整除2')
else:
    print('你输入的数字不能整除3也不能整除2')n
#elif num3%3 !=0:
#    print('你输入的数字不能整除3也不能整除2')
'''

'''
#6:if,else,elif综合练习，输入两个数，并判断他们的大小
num11=int(input('请输入第一个数 '))
num22=int(input('请输入第二个数 '))
if num11==num22:
    print('数字1和数字2相等欸')
elif num11>num22:
    print('数字1大于数字2')
else:
    print('数字1小于数字2')
'''

#7:大小判断简便写法
x=int(input("输入第一个数："))
y=int(input("输入第二个数："))
z=int(input("输入第三个数："))
a=(x if x>y else y)
print(a if a>z else z)

