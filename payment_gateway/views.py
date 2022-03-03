from locale import currency
from django.shortcuts import redirect, render
from django.conf import settings
import stripe

from traderequest.models import TradeRequest

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.

def payment(request):
    key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'payment_checkout.html', {'key': key})


def charge(request):
    buyer = request.session['username']
    k = TradeRequest.objects.get(buyer=buyer)
    if request.method == "POST":
        intent = stripe.PaymentIntent.create(
            amount=k.amount*100,
            currency='inr',
            description="Payment Gateway",
            payment_method_types=['card'],
        )
        intent['metadata'] = k.id
        clientSecret = intent['client_secret']
        return render(request, 'payment_charge.html')
    else:
        redirect('payment')
