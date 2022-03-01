from django.shortcuts import render

from transactions.models import Transactions

# Create your views here.

def get_transactions_logs(request):
    post = Transactions.objects.all()
    return render(request, 'all_transactions.html', {'post': post})


def transactions(request):
    return render(request, 'transactions.html')