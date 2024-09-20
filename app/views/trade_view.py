from django.shortcuts import render, redirect

def trading(request):
    if request.user.is_authenticated:
        context = {}

        return render(request, 'pages/trading.html', context)
    
    return redirect('create')
