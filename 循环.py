
#1：for in循环
'''
sum=0
for x in range(100):
    sum=sum+x
print(sum)
'''

#2：while循环：(注意sum和n的赋值语句先后顺序对结果的影响)
'''
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)
'''
#3：条件限定下的while循环
'''
n=1
while n<100:
    if n>10:# 当n = 11时，条件满足，执行break语句
        break# break语句会结束当前循环
    print(n)
    n=n+1
'''
#4:小练习：sum和while的方法实现1+3+5+7+9
'''
sum=0
n=1
while n<10:
    sum=sum+n
    n=n+2
print(sum)
'''

#5:打印列表1，3，5，7，9
#方法1：
'''
L=[]
n=1
while n<10:
    L.append(n)
    n=n+2
print(L)
'''
#方法2：
n=0
while n<10:
    n=n+1
    if n%2==0:# 如果n是偶数，执行continue语句
        continue# continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n) #注意此行代码是在while语句内的，如果删除前面空格，则只会打印一个数字



