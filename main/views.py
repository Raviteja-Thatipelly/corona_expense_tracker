from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST(username)
        password = request.POST(password)
        user = authenticate(request, username = username, password= password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'login sucessfull')
            return redirect(request, 'index')
        else:
            messages.error(request, 'invalid username or password')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request, "username taken")
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'email exists') 
            else:
                user = User.objects.createuser(username = username, email = email, password = password)
            user.save()
            messages.sucess(request, 'Account created sucessfully, please login')
            return redirect('login')     
        else:
            messages.error(request, 'passwords doesnot match')
    return render(request, 'register.html')

def user_logout(request):
    logout(request)
    messages.sucess(request, 'sucessfully logedout')
    return redirect('login')
    