from __future__ import unicode_literals
import string
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.conf import settings
import sqlite3, json, os, sys, platform, keyword, zipfile, zipstream, paramiko, re, shutil
import numpy as np
from rest_framework import viewsets
from demo.serializers import UserSerializer, GroupSerializer, tableDataSerializer
from demo.models import tableData
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class tableDataViewSet(viewsets.ModelViewSet):
    queryset = tableData.objects.all()
    serializer_class = tableDataSerializer


BASE_DIR = os.getcwd()


def ISplatform(request):
    if platform.system().lower() == 'windows':
        folderPath = BASE_DIR + '\\demo\\static\\upload'
    elif platform.system().lower() == 'linux':
        folderPath = BASE_DIR + '/demo/static/upload'
    return folderPath


def things(request):
    print(request.user.get_all_permissions())
    return render(request, 'thingFuncBtn.html')


def addData(request):
    return render(request, 'addData.html')


def sendData(request):
    if request.method == 'POST':
        dataobj = request.POST.get("data")
        thTitle = eval(dataobj).get('thName')
        tableTitle = eval(dataobj).get('tableName')
        tdData = eval(dataobj).get('TD_data')
        try:
            tableData.objects.create(tableName=tableTitle, thName=thTitle, TD_data=tdData)
        except OSError as e:
            raise
        return JsonResponse("{'status':200}", safe=False)


def updateData(request):
    if request.method == 'POST':
        dataobj = request.POST.get("data")
        thTitle = eval(dataobj).get('thName')
        tableTitle = eval(dataobj).get('tableName')
        tdData = eval(dataobj).get('TD_data')
        try:
            tableData.objects.filter(tableName=tableTitle).update(thName=thTitle, TD_data=tdData)
        except OSError as e:
            raise
        return JsonResponse("{'status':200}", safe=False)


def searchData(request):
    return render(request, 'searchData.html')


def editData(request):
    return render(request, 'editData.html')


# def editData(request):
#     conn = sqlite3.connect('./db.sqlite3')
#     cursor = conn.cursor()
#     cursor.execute("select name from sqlite_master where type='table' order by name")
#     alltableName = cursor.fetchall()
#     tableArr = []
#     for key in alltableName:
#         if 'table_' in key[0]:
#             tableArr.append(key[0])
#     cursor.close()
#     # return render(request,'editData.html',{'tableArr':tableArr})
#     return JsonResponse({'tableArr':tableArr})

# def sendData(request):
#     dataobj = request.POST.get("data")
#     conn = sqlite3.connect('./db.sqlite3')
#     cursor = conn.cursor()
#     str = ' text,'
#     thTitle = str.join(eval(dataobj).get('thName'))
#     tableName = "table_" + eval(dataobj).get('tableName')
#     if keyword.iskeyword(tableName):
#         cursor.close()
#         return redirect('/things/addData/')
#         # return JsonResponse(dict(msg='failed'))
#     else:
#         sql = 'create table '+ tableName + ' (id int PRIMARY KEY,%s text)' % thTitle
#         cursor.execute(sql)
#         cursor.close()
#         return redirect('/things/editData/')
# return JsonResponse(dict(msg='successful'))

def documents(request):
    # print(request.user.get_all_permissions())
    folderPath = ISplatform(request)
    Path = folderPath
    if request.user.has_perm('auth.admin'):
        Path = folderPath
    elif request.user.has_perm('auth.manager'):
        if platform.system().lower() == 'windows':
            Path = folderPath + '\\IT'
        elif platform.system().lower() == 'linux':
            Path = folderPath + '/IT'
    elif request.user.has_perm('auth.personal'):
        if platform.system().lower() == 'windows':
            Path = folderPath + '\\personal'
        elif platform.system().lower() == 'linux':
            Path = folderPath + '/personal'
    filelist = scanfile(Path)
    return render(request, 'documents.html', {'url': json.dumps(filelist)})


def upload(request):
    upTOpath = request.POST.get('upTOpath')
    if platform.system().lower() == 'windows':
        toPaht = upTOpath.replace('/', '\\\\')
    if request.method == 'GET':
        return HttpResponse('get')
    elif request.method == 'POST':
        folderPath = ISplatform(request)
        files = request.FILES.getlist('file_obj')
        pathlist = request.POST.getlist('paths')
        for file in files:
            position = os.path.join(os.path.abspath(os.path.join(folderPath + toPaht)),
                                    '/'.join(pathlist[files.index(file)].split('/')[:-1]))
            if not os.path.exists(position):
                os.makedirs(position)
            storage = open(position + '/' + file.name, 'wb+')
            for chunk in file.chunks():
                storage.write(chunk)
            storage.close()
        # shutil.move(folderPath, "C:\\b")

        return HttpResponse('ok')


def scanfile(path):
    filelist = os.listdir(path)
    allfile = {}
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            if platform.system().lower() == 'windows':
                allfile[filename] = scanfile(path + '\\' + filename)
            elif platform.system().lower() == 'linux':
                allfile[filename] = scanfile(path + '/' + filename)
        else:
            allfile[filename] = filepath
    return allfile


def checks(request):
    return render(request, 'a.html')


def zip_dir(dirname, zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for dir in dirs:
                filelist.append(os.path.join(root, dir))
            for name in files:
                filelist.append(os.path.join(root, name))

    with zipfile.ZipFile(zipfilename, "w", zipfile.ZIP_DEFLATED) as zf:
        for tar in filelist:
            print('-----' + tar + '------')
            arcname = tar[len(dirname):]
            print(tar + " -->rar: " + arcname)
            zf.write(tar, arcname)
        zf.close()
    return zipfilename


def downloadFile(request):
    dirPaths = json.loads(request.POST.get('data'))['dirPath']
    zipFileName = json.loads(request.POST.get('data'))['zipName']
    PATH = ISplatform(request).split('upload')[0]
    splitStr = '/'
    if platform.system().lower() == 'windows':
        dirPath = dirPaths.replace('/', '\\')
        zipfileDir = BASE_DIR + '\\'
        zipTOdownload = PATH + 'download\\'
        splitStr = "\\"
    else:
        dirPath = dirPaths
        zipfileDir = BASE_DIR + '/';
        zipTOdownload = PATH + 'download\\'
    try:
        if os.path.isfile(PATH + dirPath):
            print(PATH + dirPath)
            print(zipTOdownload)
            if os.path.exists(PATH + dirPath.replace('upload', 'download')):
                os.remove(PATH + dirPath.replace('upload', 'download'))
            shutil.copy2(PATH + dirPath, zipTOdownload)
            return JsonResponse("{'filetype':'file'}", safe=False)
        else:
            zip_dir(PATH + dirPath, zipFileName)
        if os.path.exists(zipTOdownload + zipFileName):
            os.remove(zipTOdownload + zipFileName)
        shutil.move(zipfileDir + zipFileName, zipTOdownload)
    except OSError as e:
        raise
    return JsonResponse("{'statusCode':'200'}", safe=False)


def deleteFile(request):
    dirPaths = json.loads(request.POST.get('data'))['dirPath']
    if platform.system().lower() == 'windows':
        dirPath = dirPaths.replace('/', '\\')
    else:
        dirPath = dirPaths
    folderPath = ISplatform(request)
    if os.path.isfile(folderPath + dirPath.split('upload')[1]):
        os.remove(folderPath + dirPath.split('upload')[1])
    else:
        shutil.rmtree(folderPath + dirPath.split('upload')[1])
    return JsonResponse("{'statusCode':'200'}", safe=False)
