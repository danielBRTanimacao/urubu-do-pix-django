from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def create(request):
    context = {
        'site_title': 'Registrar - Urubu do pix'
    }

    return render(request, 'pages/index.html', context)
    
def login_view(request):
    context = {
        'site_title': 'Login - Urubu do pix'
    }

    return render(request, 'pages/index.html', context)

@login_required(login_url='login')
def logout(request):    
    return render(request, 'pages/index.html')