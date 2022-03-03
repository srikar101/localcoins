from enum import unique
from string import ascii_uppercase
from django.shortcuts import redirect, render
from account.models import Register

from traderequest.models import TradeRequest
from advertisements.models import Advertisements
import random
import string

# Create your views here.

def get_traderequest(request):
    post = TradeRequest.objects.all()
    return render(request, 'traderequest.html', {'post': post})

def user_buy_request(request,user):
    username = Register.objects.get(username=user)
    post = Advertisements.objects.get(user=username,type='Sell')
    return render(request, 'user_buy_request.html', {'post': post})

def generate_unique_id():
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

def send_traderequest(request,id):
    obj = Advertisements.objects.get(id=id)
    if request.method == "POST":
        buyer = request.session['username']
        seller = obj.user.username
        amount = request.POST['price']
        payment_method = obj.payment_method
        unique_id = generate_unique_id()
        exchange_rate = obj.rate
        k = TradeRequest(seller=seller,buyer=buyer,unique_id=unique_id,
        amount=amount,payment_method=payment_method,exchange_rate=exchange_rate)
        k.save()
        price = int(k.amount)
        return render(request, 'payment_checkout.html', {'price': price})


    else:
        return redirect('userbuyrequest')


    