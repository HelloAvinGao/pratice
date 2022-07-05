#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
import tkinter
from tkinter import filedialog
import os, win32clipboard
 
root_window = tkinter.Tk()
root = tkinter.PanedWindow(root_window)
root.pack()
# 定义回调函数，当用户点击窗口x退出时，执行用户自定义的函数
def QueryWindow():
    # 显示一个警告信息，点击确后，销毁窗口
    result=tkinter.messagebox.askokcancel ("提示"," 你确定要关闭窗口吗? ")

    if result:
    # 这里必须使用 destory()关闭窗口
        root_window.destroy()


def gui_init():
    
    # title
    root_window.title("window title")
    # 是否拉伸
    root_window.resizable(False,False)
    # window size and position
    screenWidth = root_window.winfo_screenwidth()
    screenHeight= root_window.winfo_screenheight()

    w_width = 480
    w_height = 360
    x = (screenWidth-w_width) / 2
    y = (screenHeight-w_height) / 2
    root_window.geometry("%dx%d+%d+%d" %(w_width,w_height,x,y))

    # icon
    root_window.iconbitmap('./static/img/record_video.ico')
    # background color 
    root_window.config(background="#ebf2fa")

    # 使用协议机制与窗口交互，并回调用户自定义的函数
    root_window.protocol('WM_DELETE_WINDOW', QueryWindow)



path=StringVar()
path.set(os.path.abspath("."))
def components():
    Label(root).grid(row=0,column=0)
    Label(root, text="目标路径:").grid(row=1,column=0)
    Entry(root, textvariable=path).grid(row=1,column=1)

    Button(root, text="选择目录", command=selectPath).grid(row=1,column=2)
    Button(root, text="复制路径", command=send_to_clibboard).grid(row=1,column=3)

def selectPath():
    tempPath = filedialog.askdirectory()
    global path
    path.set(tempPath)

def send_to_clibboard():  
    win32clipboard.OpenClipboard() 
    win32clipboard.EmptyClipboard() 
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT,path.get())  
    win32clipboard.CloseClipboard()

gui_init()
components()

root_window.mainloop()