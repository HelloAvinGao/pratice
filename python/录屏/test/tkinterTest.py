#!/usr/bin/python
# -*- coding: UTF-8 -*-

from msilib.schema import Component
from struct import pack
from tkinter import *
from tkinter import messagebox
import tkinter
from turtle import position, title, width, window_width
 
def test():
    print("run here")

root_window = tkinter.Tk()

# 定义回调函数，当用户点击窗口x退出时，执行用户自定义的函数
def QueryWindow():
    # 显示一个警告信息，点击确后，销毁窗口
    if messagebox.showwarning("警告","出现了一个错误"):
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
    # config 
    btn = Button(text='button',padx=5,pady=5,command=btnCallback)
    btn.config(bd=5)
    btn.config(cursor='gumby')
    btn.config(bg='green',fg='yellow')
    btn.config(font=("Times", 15, "bold"))
    
    btn.pack()

    # the width or height of the window or Component
    root_window.update()
    print(btn.winfo_width())
    print(btn.winfo_height())

    #添加文本内容,并对字体添加相应的格式 font(字体,字号,"字体类型")
    text=tkinter.Label(root_window,text="C语言中文网，网址：c.biancheng.net",bg="yellow",fg="red",font=('Times', 15, 'bold italic underline'))
    #将文本内容放置在主窗口内
    text.pack()

    # 使用协议机制与窗口交互，并回调用户自定义的函数
    root_window.protocol('WM_DELETE_WINDOW', QueryWindow)
# PhotoImage need be global Variable
photo = tkinter.PhotoImage(file="./static/img/心型.png") 
def components():
    # pack和grid一个程序只能用一种
    # pack()
    lb_green = Label(root_window,text="绿色",bg="green",fg='#ffffff',relief=RAISED)
    # 将 黄色标签所在区域都填充为黄色，当使用 fill 参数时，必须设置 expand = 1，否则不能生效
    lb_green.pack()

    # grid()
    #tkinter.Label(root_window,text="C语言中文网",fg='blue',font=('楷体',12,'bold')).grid(row=0,column=11)

    # place()
    Label3 = Label (root_window, text="位置3",bg='green',fg='white')
    # 设置水平起始位置相对于窗体水平距离的0.6倍，垂直的绝对距离为80，大小为60，30
    Label3.place(relx=0.6,y=80, width=60, height=30)

    # label
    label1 = Label(root_window,text="文本",font=('宋体',20, 'bold italic'),bg="#7CCD7C",
                 # 设置标签内容区大小
                 width=100,height=240,
                 padx=50, pady=0, 
                 borderwidth=1, relief=RAISED,
                 image=photo,compound="top"
                 )
    label1.pack()
    Button(root_window,image=photo,command=test).pack(side="bottom")

def test():
    messagebox.showinfo(title='温馨提示', message='欢迎使用C语言中文网')
gui_init()
components()

root_window.mainloop()