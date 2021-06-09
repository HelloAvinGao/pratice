from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.conf import settings
import platform
import json
import os, sys

BASE_DIR = os.getcwd()
def ISplatform(request):
    if platform.system().lower() == 'windows':
        folderPath = BASE_DIR + '\\demo\\static\\'
    elif platform.system().lower() == 'linux':
        folderPath = BASE_DIR + '/demo/static/'
    return folderPath

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
            if platform.system().lower() == 'windows':
                allfile[filename] = scanfile(path + '\\' + filename + "\\")
            elif platform.system().lower() == 'linux':
                allfile[filename] = scanfile(path + '/' + filename + "/")
        else:
            allfile[filename] = filepath
    return allfile

def uploadfile(request):
    try:
        upFile = request.FILES.get('uploadFile')
        folderPath = ISplatform(request)
        f = open(os.path.join(folderPath + upFile.name),'wb')
        for chunk in upFile.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('ok')
    except Exception or IndexError or ValueError as ex:
        raise

def doc(request):
    folderPath = ISplatform(request)
    filelist = scanfile(folderPath)
    # print(request.user.get_all_permissions())
    # if(request.user.has_perm('demo.admin')):
    #     permissionsIS = 'admin'
    # elif(request.user.has_perm('demo.manager')):
    #     permissionsIS = 'manager'
    # else:
    #     permissionsIS = 'personal'
    return render(request,'doc.html',{'url':json.dumps(filelist)})


def user(request):
    return render(request,'user.html')

def sendAjax(request):
    dataobj = request.POST.get("data")
    path = os.getcwd()
    with open(os.path.join(path + "\\demo\\static\\tableData.json"),'w') as g:
        g.write(str(dataobj))
        g.close()
    return render(request,'things.html',{"obj":dataobj})
