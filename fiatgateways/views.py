from django.shortcuts import render,redirect

from fiatgateways.models import FiatGateways
from cryptocurrency.models import Cryptocurrency

# Create your views here.

def fiat_gateways(request):
    post = FiatGateways.objects.all()
    return render(request, 'admin_gateways.html', {'post': post})

def add_gateways(request):
    if request.method == 'POST':
        gateways_name = request.POST['name']
        slug = request.POST['slug']
        supported_currencies = request.POST['supported_currencies']
        k = FiatGateways(gateways_name=gateways_name, slug=slug, supported_currencies=supported_currencies)
        k.save()
        return redirect('fiatgateways')
    return render(request, 'add_gateways.html')

def edit_gateway(request,id):
    obj = FiatGateways.objects.get(id=id)
    if request.method == "POST":
        gateways_name = request.POST['name']
        slug = request.POST['slug']
        supported_currencies = request.POST['supported_currencies']
        FiatGateways.objects.filter(id=id).update(gateways_name=gateways_name, slug=slug,
         supported_currencies=supported_currencies)

        return redirect('fiatgateways')
    else:
        return render(request, 'edit_gateway.html', {'obj': obj})

    