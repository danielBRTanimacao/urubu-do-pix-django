from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import User
from decimal import Decimal, InvalidOperation  

@login_required(login_url='login')
def trading(request):
    if request.method == "POST":
        user = get_object_or_404(User, pk=request.user.id)
        value_deposited = request.POST.get('depositedValue')
        try:
            if Decimal(value_deposited) <= 0:
                text: str = f"Valor depositado invalido tente um valor positivo! - R${value_deposited}"
                messages.error(request, text)
                return redirect('trading')
        except InvalidOperation:
            text: str = f"O valor não pode ser um texto! - Tente novamente"
            messages.error(request, text)
            return redirect('trading')

        user.amount += Decimal(value_deposited)
        user.save()

        text: str = f"Valor depositado com sucesso! - R${value_deposited}"
        messages.success(request, text)
        return redirect('trading')

    context = {
        "title_site": 'Urubu do pix - trade',
    }

    return render(request, 'pages/trading.html', context)