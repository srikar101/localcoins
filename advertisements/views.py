from django.shortcuts import redirect, render

from advertisements.models import Advertisements
from account.models import Register

# Create your views here.

def get_advertisements(request):
    username = request.session.get('username')
    print(username)
    user = Register.objects.get(username=username)
    post = Advertisements.objects.filter(user=user)
    return render(request, 'my_advertisement.html',{'post': post})

def latest_advertisement(request):
    post = Advertisements.objects.all()
    n = len(post)
    if n>=5:
        p = Advertisements.objects.order_by('id')[n-5:]
    else:
        p = Advertisements.objects.all()
    
    print(n)
    return render(request, 'latest_advertisement.html', {'post': p})

def new_advertisement(request):
    return render(request, 'new_advertisement.html')

def post_advertisement(request):
    if request.method == 'POST':
        username = request.session.get('user_id')
        print(username)
        user = Register.objects.get(id=username)
        type = request.POST['type_of']
        crypto_currency = request.POST['cryptocurrency']
        payment_method = request.POST['paymentmethod']
        currency = request.POST['currency']
        margin = request.POST['margin']
        payment_window = request.POST['paymentwindow']
        min_limit = request.POST['minlimit']
        max_limit = request.POST['maxlimit']
        rate = request.POST['priceequation']
        payment_details = request.POST['paymentdetails']
        terms_of_trade = request.POST['termsoftrade']
        k = Advertisements(user=user,type=type,crypto_currency=crypto_currency,payment_method=payment_method,currency=currency,
        margin=margin,payment_window=payment_window,min_limit=min_limit,max_limit=max_limit,rate=rate,payment_details=payment_details,terms_of_trade=terms_of_trade)
        k.save()
        return redirect('newadd')
        
    