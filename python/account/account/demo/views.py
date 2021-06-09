from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
import os, sys
from django.conf import settings
import platform
import json

def ISplatform(request):
    if platform.system().lower() == 'windows':
        isplatform = 'windows'
    elif platform.system().lower() == 'linux':
        isplatform = 'linux'
    return isplatform

BASE_DIR = os.getcwd()
folderPath = BASE_DIR + '\\demo\\static\\'
def things(request):
    return render(request,'things.html')

def home(request):
    return render(request,'home.html')

def scanfile(path):
    filelist = os.listdir(path)
    allfile={}
    for filename in filelist:
        filepath = os.path.join(path,filename)
        if os.path.isdir(filepath):
            allfile[filename] = scanfile(path + '\\' + filename + "\\")
        else:
            allfile[filename] = filepath
    return allfile

def uploadfile(request):
    # try:
        upFile = request.FILES.get('uploadFile')
        print(str(upFile))
        path = os.getcwd()
        f = open(os.path.join(path + "\\demo\\static\\DOC\\" + upFile.name),'wb')
        for chunk in upFile.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('ok')
    # except Exception or IndexError or ValueError as ex:
    #     print(ex.args)
    #     return HttpResponse("文件格式不对，请查看后上传")

def doc(request):
    global folderPath
    filelist = scanfile(folderPath)
    return render(request,'doc.html',{'url':json.dumps(filelist)})


def user(request):
    print(request.path_info)
    return render(request,'user.html',{'url':request.path_info})

def sendAjax(request):
    try:
        num1 = request.POST.get("data")
        path = os.getcwd()
        print(str(num1))
        with open(os.path.join(path + "\\demo\\static\\tableData.json"),'w') as g:
            g.write(str(num1))
            g.close()
        return redirect('/things/')
    except Exception as e:
        return HttpResponse(e)
