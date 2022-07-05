#!/usr/bin/python
# -*- coding: UTF-8 -*-

from msilib.schema import Component
from struct import pack
from tkinter import *
from tkinter import messagebox
import tkinter
from turtle import position, title, width, window_width
 
root_window = tkinter.Tk()
# 定义回调函数，当用户点击窗口x退出时，执行用户自定义的函数
def QueryWindow():
    # 显示一个警告信息，点击确后，销毁窗口
    result=tkinter.messagebox.askokcancel ("提示"," 你确定要关闭窗口吗? ")

    if result:
    # 这里必须使用 destory()关闭窗口
        root_window.destroy()

def btnCallback():
    messagebox.showwarning("警告","run here")

def gui_init():
    
    # title
    root_window.title("window title")
    # 是否拉伸
    root_window.resizable(False,False)
    # window size and position
    screenWidth = root_window.winfo_screenwidth()
    screenHeight= root_window.winfo_screenheight()

    w_width = 960
    w_height = 720
    x = (screenWidth-w_width) / 2
    y = (screenHeight-w_height) / 2
    root_window.geometry("%dx%d+%d+%d" %(w_width,w_height,x,y))

    # icon
    root_window.iconbitmap('./static/img/record_video.ico')
    # background color 
    root_window.config(background="#ebf2fa")

    # 使用协议机制与窗口交互，并回调用户自定义的函数
    root_window.protocol('WM_DELETE_WINDOW', QueryWindow)

entryVar=StringVar() 
entry2Var=StringVar() 
textVar=StringVar() 
v=IntVar()
def components():
    # 新建文本标签
    labe1 = tkinter.Label(root_window,text="账号：")
    labe2 = tkinter.Label(root_window,text="密码：")
    # grid()控件布局管理器，以行、列的形式对控件进行布局，后续会做详细介绍
    labe1.grid(row=0)
    labe2.grid(row=1)
    # 为上面的文本标签，创建两个输入框控件
    entry1 = tkinter.Entry(root_window,textvariable=entryVar,exportselection=0)
    entry2 = tkinter.Entry(root_window,show="*",textvariable=entry2Var,validate ="focusout",validatecommand=CheckTest)
    # 对控件进行布局管理，放在文本标签的后面
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    submitBtn = tkinter.Button(root_window,text="submit",command=submitCallback)
    submitBtn.grid(row=2,column=1)

    # 导航栏按钮
    topmenu=Menu(root_window)

    #创建文件下拉菜单，添加到顶层菜单窗口
    filemenu=Menu(topmenu,tearoff=False)

    #添加下拉内容：

    filemenu.add("command",label="打开")
    filemenu.add_command(label="保存")
    filemenu.add_command(label="另存为")
    filemenu.add_separator()
    filemenu.add_command(label="页面设置")
    filemenu.add_command(label="打印")
    filemenu.add_separator()
    filemenu.add_command(label="退出")
    topmenu.add_cascade(label="文件",menu=filemenu)

    #跟窗口显示菜单栏
    root_window.config(menu=topmenu)

    # 创建一个文本控件
    # width 一行可见的字符数；height 显示的行数
    text = Text(root_window, width=50, height=30, undo=True, autoseparators=False,exportselection=False,wrap=WORD)
    # 适用 pack(fill=X) 可以设置文本域的填充模式。比如 X表示沿水平方向填充，Y表示沿垂直方向填充，BOTH表示沿水平、垂直方向填充
    text.grid(row=3, column=2, sticky="w", padx=10, pady=5)
    # INSERT 光标处插入；END 末尾处插入
    text.insert(INSERT, 'C语言中文网，一个有温度的网站')

    # radio Button
    # 根据单选按钮的 value 值来选择相应的选项
    v.set(0)
    # 使用 variable 参数来关联 IntVar() 的变量 v
    tkinter.Radiobutton(root_window, text="C语言中文网", fg='blue',font=('微软雅黑','12','bold'),variable=v, value=0).grid(row=6)
    tkinter.Radiobutton(root_window, text="CSDN平台", variable=v, value=2).grid(row=7)
    tkinter.Radiobutton(root_window, text="知乎平台", variable=v, value=3).grid(row=8)
    tkinter.Radiobutton(root_window, text="牛客网平台",command = select, variable=v, value=4).grid(row=9)

def submitCallback():
    print(entryVar.get())

def CheckTest():
    print(entry2Var.get())
    print("run here entry2")

def select():
    dict = {1:'C语言中文网',2:'菜鸟教程',3:'W3SCHOOL',4:'微学苑'}
    strings = '您选择了' + dict.get(v.get()) + '，祝您学习愉快'
    print(strings)

gui_init()
components()

print(textVar.get())
root_window.mainloop()