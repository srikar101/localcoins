import email
from pdb import post_mortem
from django.shortcuts import redirect, render
from account.models import Register
from advertisements.models import Advertisements

from cryptocurrency.models import Cryptocurrency
from fiatcurrency.models import FiatCurrency
from fiatgateways.models import FiatGateways
from traderequest.models import TradeRequest
from transactions.models import Transactions

# Create your views here.

def admin_page(request):
    return render(request, 'adminpage.html')

def crypto_currency(request):
    post = Cryptocurrency.objects.all()
    return render(request, 'admin_crypto.html', {'post': post})

def add_crypto(request):
    if request.method == 'POST':
        crypto_name = request.POST['name']
        crypto_code = request.POST['code']
        crypto_symbol = request.POST['symbol']
        crypto_image = request.POST['image']
        crypto_rate = request.POST['rate']
        k = Cryptocurrency(crypto_name=crypto_name, crypto_code=crypto_code, crypto_symbol=crypto_symbol,
        crypto_rate=crypto_rate, crypto_image=crypto_image)
        k.save()
        return redirect('cryptocurrency')
    return render(request, 'add_crypto.html')

def edit_crypto(request,id):
    obj = Cryptocurrency.objects.get(id=id)
    if request.method == "POST":
        crypto_name =request.POST['name']
        crypto_code = request.POST['code']
        crypto_symbol = request.POST['symbol']
        crypto_image = request.POST['image']
        crypto_rate = request.POST['rate']
        Cryptocurrency.objects.filter(id=id).update(crypto_name=crypto_name,crypto_code=crypto_code,crypto_symbol=crypto_symbol,
        crypto_image=crypto_image,crypto_rate=crypto_rate)
        return redirect('cryptocurrency')
    else:
        return render(request, 'edit_crypto.html', {'obj': obj})




def trade_request(request):
    post = TradeRequest.objects.all()
    return render(request, 'admin_traderequest.html', {'post': post})

def all_users(request):
    post = Register.objects.all()
    return render(request, 'all_users.html', {'post': post})

def edit_user(request,id):
    obj = Register.objects.get(id=id)
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        country = request.POST['country']
        created_datetime = request.POST['created_datetime']
        Register.objects.filter(id=id).update(username=username,email=email,mobile_number=mobile_number,
        country=country,created_datetime=created_datetime)
        return redirect('allusers')
    return render(request, 'edit_user.html', {'obj': obj})

def delete_user(request,id):
    obj = Register.objects.get(id=id)
    obj.delete()
    return redirect('allusers')

def all_advertisement(request):
    post = Advertisements.objects.all()
    return render(request, 'admin_advertisement.html', {'post': post})




def all_transaction(request):
    post = Transactions.objects.all()
    return render(request, 'admin_transaction.html', {'post': post})

def dashboard(request):
    return render(request, 'admin_dashboard.html')