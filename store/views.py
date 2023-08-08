from django.shortcuts import render,redirect
from .import views
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Product

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def cycle(request):
    dict_cycle={
        'cycle':Product.objects.all()
    }
    return render(request,'cycle.html',dict_cycle)
def newsv(request):
    return render(request,'news.html')
def contacts(request):
      return render(request,'contact.html')
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Login")
            return redirect('login')

    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"Username Already Exists")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email Already Used")
            return redirect('register')
        else:    
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('/')
    else:
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

