# 在这里写上你的代码 :-)
text= 'this is my first test.\n This is next line.\n This is last line.'#注意是\而不是/
print(text)
#'w'代表write，以可编写方式打开。‘r’代表read,以只读模式打开，不可编写。
#第一步打开，第二步编写，第三步关上
my_file=open('my_file.txt','w')#.txt前的名字可以任意设定。
my_file.write(text)
#一定要用下面代码关上，否则会生成一个空文本。
my_file.close()
#运行结果会在桌面生成一个文本文件。
#若只在桌面生成一个文本，不在此处查看结果，第三行的print语句可不用


