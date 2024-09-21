from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from app.forms import RegisterForm, LoginForm

def create(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'site_title': 'Registrar - Urubu do pix',
        'form': form
    }

    return render(request, 'pages/create.html', context)
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('account')
        
    context = {
        'site_title': 'Login - Urubu do pix',
        'form': form 
    }

    return render(request, 'pages/login.html', context)

@login_required(login_url='login')
def logout_view(request):    
    logout(request)
    return redirect('login')