#调用tkinter创建click me 按钮
from tkinter import *
tk=Tk()
btn=Button(tk, text='click me')
btn.pack()
#实现按下按钮，显示hello there的效果
def hello():
    print('hello there')
from tkinter import *
tk=Tk()
btn=Button(tk,text='click me', command=hello)
btn.pack()