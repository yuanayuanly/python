'''若桌面原本就存在一个名为myfile的文本，则下面代码会往文本中添加文字，
若没有，执行n次则会在同一个文本中出现n行相同的文字'''
append_text='\n This is append file.'
my_file=open('myfile.txt','a')
my_file.write(append_text)
my_file.close()
print(append_text)#注意括号中输入的内容，输入my_file无反应。
