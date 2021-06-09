# -*- coding:utf-8 -*-

import psutil
import time

from threading import Lock

from flask import Flask, render_template, session, request
from flask_socketio import SocketIO
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)


count = 0
while True:
    socketio.sleep(2)
    t = time.strftime('%M:%S', time.localtime()) # 获取系统时间（只取分:秒）
    cpus = psutil.cpu_percent(interval=None) # 获取系统cpu使用率 non-blocking
    print(cpus)



