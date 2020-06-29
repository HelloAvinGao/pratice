from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from django.contrib  import  auth#引入auth模块
from django.contrib.auth.models import User # auth应用中引入User类
from django.contrib.auth.decorators import login_required
from demo import models
from demo.models import Register
# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('userPassword')
        telephone = request.POST.get('userPhone')
        email = request.POST.get('userEmail')
        gender = request.POST.get('userGender')
        age = '2'
        user = Register.objects.create(age=age, username=username, password=password, email=email, gender=gender, mobile=telephone)
        return HttpResponseRedirect("/accounts/login/")

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('userPassword')
        print(username)
        print(password)
        user_obj = auth.authenticate(username=username, password=password)
        print(user_obj)
        if user_obj:
            auth.login(request, user_obj)
            return HttpResponseRedirect("/index/")
        else:
            return render(request,'login.html', {'error_msg':'error account!'})

@login_required
def index(request):
    if request.user.is_authenticated:#调用request.user的is_authenticated伪方法进行认证
        print(request.user)#request.user就是当前用户对象，打印结果为用户名称
        if request.method == 'GET':
            return render(request, 'index.html', locals())
    else:
        return redirect('/accounts/login/')


#注销功能，清除掉cookie和session，
def log_out(request):
    #登录的时候，用到了login()函数，
    auth.logout(request)#清除了cookie和session，清除了当前的用户，
    return redirect("/accounts/login/")

