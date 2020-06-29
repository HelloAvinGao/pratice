from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.core import signing
from django_redis import get_redis_connection
from django.core.cache import cache
from django.contrib.auth import authenticate, login
from django.contrib  import  auth
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    value = signing.dumps({"foo": "bar"})
    src = signing.loads(value)
    print(value)
    print(src)
    # request.set_cookie('key_test','value_hello')
    #     # values = request.COOKIES['key_test']
    #     # print(values)

    cache.set('index_page_data', 'cache_value', 30)
    values = cache.get('index_page_data')
    print(values)

    user = request.COOKIES.get('username') #从cookie中取值
    if user:
        return render(request, 'index.html', {'user':user})
    else:
        return redirect('/login/')

def session_test(request):
    # request.session['h1']='hello'
    h1 = request.session.get('h1')
    return HttpResponse(h1)

def cookie_test(request):
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u == 'alex' and p == 'wuwowuji521':
            red = redirect('/index/')  #登录成功，则重定向到index
            red.set_cookie('username', u) #将用户名插入cookie
            return red
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')





