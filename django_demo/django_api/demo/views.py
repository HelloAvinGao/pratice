from django.shortcuts import render
from django.contrib.auth.models import User,Group
from demo.models import Test,Book
from rest_framework import viewsets
from demo.api import UserSerializer,GroupSerializer,TestSerializer,BookSerializer

from django.http import HttpResponse
import json
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API 允许查看或编辑用户
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API 允许查看或编辑组
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

def login(request):
    context          = {}
    context['hello'] = 'Hello World!'
    context['gao'] = 'gao World!'
    return render(request, 'index.html', {"context":context})

 
 
# 定义功能
def add_args(a, b):
    return a+b
 
# 接口函数
def post(request):
    if request.method == 'POST':  # 当提交表单时
        dic={}
        # 判断是否传参
        if request.POST:
            a= request.POST.get('a', 0)
            b = request.POST.get('b', 0)
            # 判断参数中是否含有a和b
            if a and b:
                res = add_args(a, b)
                dic['number'] = res
                dic = json.dumps(dic)
                obj = HttpResponse(dic)
                obj['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
                return obj
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
 
    else:
        return HttpResponse('方法错误')
