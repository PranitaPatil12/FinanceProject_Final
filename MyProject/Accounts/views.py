from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def loginview(request):
    print(request.POST)
    if request.method == 'POST':
        print(request.method)
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        print(un,pw)
        user=authenticate(username=un,password=pw)
        print(user)
        print("About to login")
        if user is not None:
            print('logined')
            login(request,user)
            return redirect('adminhomepg')
        else:
            messages.error(request,'Invalid Login Id or Password')
    template_name = 'login.html'
    context = {}
    return render(request, template_name, context)


def logoutview(request):
    logout(request)
    return redirect('loginpage1')
