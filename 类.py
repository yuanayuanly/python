'''对事物进行广义的分类，比如说人是一个类，动物也可以分成一个类，
类有自己的属性，比如人有男女，动物有公母的属性，类中可以调用自己的属性'''
class Calculator:
    name='good calculator'
    #类中可以调用自己的属性
    price=18
    def add(self,x,y):
        #自定义函数记得加冒号
        print(self.name)
        result=x+y
        print(result)
    def minus(self,x,y):
        print(self.price)
        print(x-y)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)
'''运行后可在结果中输入下面指令
cal=Calculator()#将类用缩写变量名代替，记得类名称要带()
cal.name
cal.price
cal.add(20,10)
.....'''


