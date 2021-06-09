from django.shortcuts import render

# Create your views here.
def login(request):
    result = {'error': 'Your username or password is wrong!Please input it again'}
    return render(request,'form.html')