from django.shortcuts import render

from traderequest.models import TradeRequest

# Create your views here.

def get_traderequest(request):
    post = TradeRequest.objects.all()
    return render(request, 'all_traderequest.html', {'post': post})

def send_trade(request):
    post = TradeRequest.objects.all()
    return render(request, 'traderequests.html',{'post': post})