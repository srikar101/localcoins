from itertools import count
from django.shortcuts import render
from account.models import Register
from advertisements.models import Advertisements
from account.middleware import auth_middleware


# Create your views here.


def dashboard(request):
    id = request.session['user_id']
    username = request.session['username']
    my_details = Register.objects.get(username=username)
    my_adv = Advertisements.objects.filter(user=my_details)
    print(my_adv)
    num_adv = my_adv.count()
    context = {'my_details': my_details, 'my_adv': my_adv, 'num_adv': num_adv}
    return render(request, 'dashboard.html', context)

@auth_middleware
def user_auth(request):
    print(request.session.get('email'))
    return render(request, 'user_auth.html')