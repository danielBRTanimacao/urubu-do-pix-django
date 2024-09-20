from django.shortcuts import render, redirect

def index(request):
    context = {
        'title_site': 'Urubu do pix'
    }

    return render(request, 'pages/index.html', context)

def account(request):
    if request.user.is_authenticated:
        context = {}

        return render(request, 'pages/account.html', context)

    return redirect('create')
