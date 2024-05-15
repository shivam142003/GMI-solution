from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .import views

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def Aboutus(request):
    return render(request,'Aboutus.html')

def register(request):
    if request.method =='POST':
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        password2=request.POST["password2"]

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exist')
                return redirect(register)
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist')
                return redirect(register)
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'invalid password')
            return redirect(register)
    else:
        return render(request,'register.html')

def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        user= auth.authenticate(email=email,password=password)    

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Not registered')
            return redirect('login')
    else:
        return render(request,'login.html')
