from locale import currency
from django.shortcuts import redirect, render
from LOCALCOINS.views import home
from account.models import Register
from advertisements.models import Advertisements
# Create your views here.


def find_offers(request):
    if request.method == "POST":
        type_of = request.POST['type']
        crypto_currency = request.POST['cryptocurrency']
        payment_method = request.POST['paymentmethod']
        currency = request.POST['currency']
        post = Advertisements.objects.filter(type=type_of,crypto_currency=crypto_currency,
        payment_method=payment_method,currency=currency)
        print(post)
        if post:
            context = {'t': type_of, 'post': post}
            return render(request, 'offers.html', context)
        else:
            return redirect('home')

def buy_crypto(request):
    type_of = "Sell"
    username = request.session['username']
    user = Register.objects.get(username=username)
    obj = Advertisements.objects.exclude(user=user)
    post = obj.filter(type=type_of)
    if post:
        return render(request, 'buy.html', {'post': post})
    return redirect('/')
        

def buy_to_allusers(request):
    type_of = "Sell"
    obj = Advertisements.objects.all()
    post = obj.filter(type=type_of)
    if post:
        return render(request, 'buy_for_allusers.html', {'post': post})
    return redirect('home')

    

def sell_crypto(request):
    type_of = "Buy"
    username = request.session['username']
    user = Register.objects.get(username=username)
    obj = Advertisements.objects.exclude(user=user)
    post = obj.filter(type=type_of)
    if post:
        return render(request, 'sell.html', {'post': post})
    return redirect('/')
        
    

def sell_to_allusers(request):
    type_of = "Buy"
    obj = Advertisements.objects.all()
    post = obj.filter(type=type_of)
    if post:
        return render(request, 'sell_for_allusers.html', {'post': post})
    return redirect('home')