#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
from tkinter import *
import tkinter
from tkinter import filedialog
import os, win32clipboard
from recordMP4 import on_press
from tkinter import messagebox
from fileinput import filename
from PIL import ImageGrab
import numpy as np
import cv2
import datetime
from pynput import keyboard

root_window = tkinter.Tk()
root = tkinter.PanedWindow(root_window)
root.pack()
# 定义回调函数，当用户点击窗口x退出时，执行用户自定义的函数
# def QueryWindow():
#     # 显示一个警告信息，点击确后，销毁窗口
#     result=tkinter.messagebox.askokcancel ("提示"," 你确定要关闭窗口吗? ")

#     if result:
#     # 这里必须使用 destory()关闭窗口
#         root_window.destroy()


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
    # root_window.protocol('WM_DELETE_WINDOW', QueryWindow)



path=StringVar()
path.set(os.path.abspath("."))
interval = 10
def components():
    Label(root).grid(row=0,column=0)
    Label(root, text="目标路径:").grid(row=1,column=0)
    Entry(root, textvariable=path).grid(row=1,column=1)

    Button(root, text="选择目录", command=selectPath).grid(row=1,column=2)
    Button(root, text="复制路径", command=send_to_clibboard).grid(row=1,column=3)

    Button(root, text="开始录制!", command=video_record).grid(row=2,column=0)
    Button(root, text="停止录制!", command=video_stop_record).grid(row=2,column=3)

def selectPath():
    tempPath = filedialog.askdirectory()
    global path
    path.set(tempPath)

def send_to_clibboard():  
    win32clipboard.OpenClipboard() 
    win32clipboard.EmptyClipboard() 
    win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT,path.get())  
    win32clipboard.CloseClipboard()


flag=False
videoName = ""
def video_record():
    th=threading.Thread(target=video_start_record)
    th.start()

def video_start_record():
    print("开始录屏!")
    name = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') #当前的时间
    global videoName
    videoName = name
    p = ImageGrab.grab()  # 获得当前屏幕
    a, b = p.size  # 获得当前屏幕的大小
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 编码格式
    video = cv2.VideoWriter('%s.avi'%name, fourcc, 20, (a, b))
    while True:
        im = ImageGrab.grab()
        imm=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
        video.write(imm)
        if flag:
            messagebox.showinfo("提示","录制结束!")
            break
    video.release()

def mp4Toimg(videoName,output_path,interval):
    num = 1
    vid = cv2.VideoCapture(videoName)
    while vid.isOpened():
        is_read, frame = vid.read()
        if is_read:
            if num % interval == 1:
                file_name = '%08d' % num
                cv2.imwrite(str(output_path) + str(file_name) + '.jpg', frame)
                cv2.waitKey(1)
            num += 1

        else:
            break


def video_stop_record():
    if videoName:
        global flag
        flag=True
        mp4Toimg('%s.avi'%videoName,path,interval)
        print("stop monitor！")
        return False
  
    else:
        messagebox.showwarning("警告","请先录制!")
    return False

gui_init()
components()

root_window.mainloop()


