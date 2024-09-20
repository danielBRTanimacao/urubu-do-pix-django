from django.shortcuts import render, redirect

def create(request):
    if request.user.is_authenticated:
        context = {}

        return render(request, 'pages/trading.html', context)
    
    return redirect('create')

def login_view(request):
    if request.user.is_authenticated:
        context = {}

        return render(request, 'pages/trading.html', context)
    
    return redirect('create')

def logout(request):    
    return render(request, 'pages/index.html')