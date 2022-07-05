#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from warnings import catch_warnings
from PIL import ImageGrab
import numpy as np
import threading,tkinter,cv2,datetime,os, win32clipboard, shutil, base64
from icon import img

root_window = tkinter.Tk()
root = tkinter.PanedWindow(root_window)
root.pack()

# tkinter页面初始化显示
def gui_init():
    # title
    root_window.title("window title")
    # 是否拉伸
    root_window.resizable(False,False)
    # window size and position
    screenWidth = root_window.winfo_screenwidth()
    screenHeight= root_window.winfo_screenheight()

    # 指定tkinter宽高
    w_width = 480
    w_height = 150
    # tkinter居中显示
    x = (screenWidth-w_width) / 2
    y = (screenHeight-w_height) / 2
    root_window.geometry("%dx%d+%d+%d" %(w_width,w_height,x,y))

    # icon
    tmp = open("tmp.ico","wb+")
    tmp.write(base64.b64decode(img))
    tmp.close()
    root_window.iconbitmap("tmp.ico")
    os.remove("tmp.ico")

    root_window.config(background="#ebf2fa")



imgPath=StringVar()
imgPath.set("")
jpgPath=""
mp4Path=StringVar()
videoPath=""
interval = 10
def components():
    Label(root).grid(row=0,column=0)

    Label(root, text="图片存放路径:").grid(row=1,column=0)
    Entry(root, textvariable=imgPath).grid(row=1,column=1)
    Button(root, text="选择目录", command=selectImgPath).grid(row=1,column=2)
    Button(root, text="清除路径", command=clearImgPath).grid(row=1,column=3)
    
    Label(root, text="视频存放路径:").grid(row=2,column=0)
    Entry(root, textvariable=mp4Path).grid(row=2,column=1)
    Button(root, text="选择目录", command=selectMp4Path).grid(row=2,column=2)
    Button(root, text="清除路径", command=clearMp4Path).grid(row=2,column=3)

    Button(root, text="开始录制视频!", command=video_record).grid(row=4,column=0)
    Button(root, text="视频转图片!", command=video_stop_record).grid(row=4,column=1)
    Button(root, text="复制图片路径", command=send_to_clibboard).grid(row=4,column=2)

    Label(root).grid(row=5,column=0)


#清空选择的图片存放路径
def clearImgPath():
    global imgPath
    imgPath.set("")
    global jpgPath
    jpgPath = ""

# 清空选择的视频文件
def clearMp4Path():
    global mp4Path
    mp4Path.set("")
    global videoPath
    videoPath = ""

# 选择图片存放文件夹路径
def selectImgPath():
    tempPath = filedialog.askdirectory()
    global imgPath
    imgPath.set(tempPath)
    global jpgPath
    jpgPath = tempPath

# 选择视频文件
def selectMp4Path():
    tempPath = filedialog.askopenfilename()
    global mp4Path
    mp4Path.set(tempPath)
    global videoPath
    videoPath = tempPath

# 将指定的图片路径添加到剪切版
def send_to_clibboard():  
    win32clipboard.OpenClipboard() 
    win32clipboard.EmptyClipboard() 
    if imgPath.get():
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT,imgPath.get()) 
    else:
        win32clipboard.SetClipboardData(win32clipboard.CF_UNICODETEXT,os.path.abspath("./")) 
    win32clipboard.CloseClipboard()


flag=False
videoName = ""
# 录制视频 引入函数
def video_record():
    th=threading.Thread(target=video_start_record)
    th.start()

# 录制视频
def video_start_record():
    print("开始录屏!")

    # 窗口最小化
    root_window.iconify()

    # 设置视频名称
    if videoPath:
        name = videoPath.split("/")[len(videoPath.split("/"))-1]
    else:
        name = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') #当前的时间
        name = '%s.avi'%name

    # 设置外部引用视频名称
    global videoName
    videoName = name
    
    # 设置视频录制终止条件
    global flag
    flag = False

    p = ImageGrab.grab()  # 获得当前屏幕
    a, b = p.size  # 获得当前屏幕的大小
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 编码格式
    video = cv2.VideoWriter(name, fourcc, 20, (a, b))
    while True:
        im = ImageGrab.grab()
        imm=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
        video.write(imm)
        if flag:
            messagebox.showinfo("提示","录制结束!")
            break
    video.release()

# 视频转图片
def mp4Toimg(videoName,output_path,interval):
    num = 1
    vid = cv2.VideoCapture(videoName)
    try:
        while vid.isOpened():
            is_read, frame = vid.read()
            if is_read:
                if num % interval == 1:
                    file_name = '%08d' % num
                    
                    # 判断当前路径是否有jpg文件
                    if os.path.exists(str(file_name) + '.jpg'):
                        os.remove(os.path.join(output_path , str(file_name) + '.jpg'))
                    
                    # MP4生成jpg图片
                    cv2.imwrite("./" + str(file_name) + '.jpg', frame)

                    # 判断是否指定图片存放地址
                    if output_path:
                        # 判断图片存放地址是否有jpg文件
                        if os.path.exists(os.path.join(output_path , str(file_name) + '.jpg')):
                            os.remove(os.path.join(output_path , str(file_name) + '.jpg'))
                        
                        # 移动当前路径下生成的jpg文件到指定路径下
                        shutil.move(str(file_name) + '.jpg', output_path)

                    cv2.waitKey(1)
                num += 1

            else:
                break
        return True
    except:
        return False

# 图片转视频
def video_stop_record():
    global videoName
    # 外部视频转图片，获取视频文件名
    if videoPath:
        videoName = videoPath
    
    # 判断视频是否存在，存在就进行视频转图片
    if videoName:
        global flag
        flag=True
        returnFlg = mp4Toimg(videoName,jpgPath,interval)
        if returnFlg:
            messagebox.showinfo("提示","图片生成成功!")
        else:
            messagebox.showwarning("警告","图片生成失败!")
  
    else:
        messagebox.showwarning("警告","请先录制!")

    return False

gui_init()
components()

root_window.mainloop()


