from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import json
import os,sys,platform

def index(request):
  return render(request,"index.html")

BASE_DIR = os.getcwd()
def ISplatform(request):
    if platform.system().lower() == 'windows':
        folderPath = BASE_DIR + '\\app\\static\\'
    elif platform.system().lower() == 'linux':
        folderPath = BASE_DIR + '/app/static/'
    return folderPath

def uploadFolder(request):
    filePath = request.POST.get('file')
    print(filePath.split('\\')[len(filePath.split('\\'))-1])
    folderZIPname = filePath.split('\\')[len(filePath.split('\\'))-1]
    folderZIPpath = filePath.split(folderZIPname)[0]+"folder.zip"
    os.system('cd %s'%folderZIPpath)
    print(folderZIPpath)
    os.system('start winrar a -ibck -k -m1 -r  -s -idq -x %s %s' %(folderZIPpath,filePath))
    #需要winrar软件搭配

    # dir = request.FILES
    # print(dir)
    # dirlist = dir.getlist('file')
    # for file in dirlist:
    #     folderPath = ISplatform(request)
    #     print(file)

    #     if not os.path.exists(folderPath):
    #         os.makedirs(folderPath)
    #     f = open(os.path.join(folderPath,file.name), 'wb+')
    #     for chunk in file.chunks():
    #         f.write(chunk)
    #     f.close()
    return HttpResponse('ok')
  # if not dirlist:
  #   return HttpResponse('files not found')
  # else:
  #
  #   for file in dirlist:
  #     position = os.path.join(os.path.abspath(os.path.join(os.getcwd(), 'projects')),
  #                             '/'.join(pathlist[dirlist.index(file)].split('/')[:-1]))
  #     if not os.path.exists(position):
  #       os.makedirs(position)
  #     storage = open(position + '/' + file.name, 'wb+')
  #     for chunk in file.chunks():
  #       storage.write(chunk)
  #     storage.close()
  #   return HttpResponse('1')