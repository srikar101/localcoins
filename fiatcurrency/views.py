from django.shortcuts import render, redirect

from fiatcurrency.models import FiatCurrency

# Create your views here.

def fiat_currencies(request):
    post = FiatCurrency.objects.all()
    return render(request, 'fiat_currencies.html', {'post': post})

def add_fiatcurrencies(request):
    if request.method == 'POST':
        fiat_name = request.POST['name']
        fiat_code = request.POST['code']
        fiat_symbol = request.POST['symbol']
        fiat_rate = request.POST['rate']
        k = FiatCurrency(fiat_name=fiat_name, fiat_code=fiat_code, fiat_symbol=fiat_symbol, fiat_rate=fiat_rate)
        k.save()
        return redirect('fiatcurrencies')
    return render(request, 'add_fiatcurrency.html')

def edit_fiatcurrency(request,id):
    obj = FiatCurrency.objects.get(id=id)
    if request.method == "POST":
        fiat_name = request.POST['name']
        fiat_code = request.POST['code']
        fiat_symbol = request.POST['symbol']
        fiat_rate = request.POST['rate']
        FiatCurrency.objects.filter(id=id).update(fiat_name=fiat_name,
         fiat_code=fiat_code, fiat_symbol=fiat_symbol, fiat_rate=fiat_rate)
        return redirect('fiatcurrencies')
    else:
        return render(request, 'edit_fiatcurrencies.html', {'obj': obj})

    
