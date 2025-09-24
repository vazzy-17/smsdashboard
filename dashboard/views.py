from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
   return render(request, 'dashboard/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'dashboard/login.html', {'error': 'Username atau password salah'})
    
    return render(request, 'dashboard/login.html')

@login_required
def home_view(request):
    return render(request, 'dashboard/home.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')