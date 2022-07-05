"""
python 屏幕录制改进版，无opencv黑框显示！
@zhou 2020/1/29_
"""
from fileinput import filename
from PIL import ImageGrab
import numpy as np
import cv2
import datetime
from pynput import keyboard
import threading
flag=False  #停止标志位
videoName = ''
out_path = './'
interval = 10
def video_record():
    """
    屏幕录制！
    :return:
    """
    print("开始录屏!")
    name = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') #当前的时间
    global videoName
    videoName = name
    p = ImageGrab.grab()  # 获得当前屏幕
    a, b = p.size  # 获得当前屏幕的大小
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 编码格式
    video = cv2.VideoWriter('%s.avi'%name, fourcc, 20, (a, b))  # 输出文件命名为test.mp4,帧率为16，可以自己设置
    while True:
        im = ImageGrab.grab()
        imm=cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
        video.write(imm)
        if flag:
            print("录制结束！")
            break
    video.release()
def on_press(key):
    """
    键盘监听事件！！！
    :param key:
    :return:
    """
    mp4Toimg('%s.avi'%videoName,out_path,interval)
    #print(key)
    global flag
    if key == keyboard.Key.esc:
        flag=True
        print("stop monitor！")
        return False  #返回False，键盘监听结束！
    
def mp4Toimg(videoName,output_path,interval):
    num = 1
    vid = cv2.VideoCapture(videoName)
    while vid.isOpened():
        is_read, frame = vid.read()
        if is_read:
            if num % interval == 1:
                file_name = '%08d' % num
                cv2.imwrite(output_path + str(file_name) + '.jpg', frame)
                # 00000111.jpg 代表第111帧
                cv2.waitKey(1)
            num += 1

        else:
            break

if __name__=='__main__':
    th=threading.Thread(target=video_record)
    th.start()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    
    