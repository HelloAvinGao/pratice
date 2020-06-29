from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request,'form.html')

def login(request):
    if request.method == "POST":
        print('run here')
        print(request.POST.get('username'))
        if  request.POST.get('username') and request.POST.get('pwd'):
            # account = {}
            # account['username'] = request.POST.get('username')
            # account['pwd'] = request.POST.get('pwd')
            return render(request,'index.html',{"name": [{'username':request.POST.get('username'),'pwd':request.POST.get('pwd')}]})
        else:
            return render(request,'form.html',{'error_msg':'username or password is error.'})
