from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def trading(request):
    context = {
        "title_site": 'Urubu do pix - trade'
    }

    return render(request, 'pages/trading.html', context)