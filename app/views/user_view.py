from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'title_site': 'Urubu do pix'
    }

    return render(request, 'pages/index.html', context)

@login_required(login_url='login')
def account(request):
    context = {
        'title_site': f'Urubu do pix - {request.user.username}'
    }
    
    return render(request, 'pages/account.html', context)