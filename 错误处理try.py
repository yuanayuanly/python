#1:报错实验，运行代码后看到file not found error
#file=open('eee.txt','r')
#2：except语句接收错误
try:
    file=open('eee.txt','r')
except Exception as e:#将错误存储在变量e中
    print(e)#将错误信息打印出来
    print('there is no file named as eee')#或者自己给出报错后的提示语句
    response=input('do you want to creat a new file')
    if response=='y':
        file=open('eee.txt','w')
    else:
        pass
        #运行并输入y后可以查看有无成功创建名为eee的文本文档
else:
    file.write('sss')
    file.close()
'''
重要注释：
r(只读),r+（只读和可写入）,w（写入）三种模式区别
上面代码执行结束后会报错，因为开始try下面的语句时r模式，后面不可写入
（1）若改为w模式，则运行后程序发现没有eee文件，然后直接创建一个，
并执行后面的代码写入'sss'(w模式下有该文件则打开，无该文件则会自动创建并打开)
（2）若改为r+模式，则运行后会提示无该文件，询问是否创建，回复y后该文件创建，但还没有写入，
此时关闭程序重新运行一次则文件中会写入'sss'
'''
