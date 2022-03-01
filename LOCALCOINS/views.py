from django.utils import translation
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.utils.translation import gettext as _

from advertisements.models import Advertisements

def home(request):
    trans = _("Hello")
    return render(request, 'home.html', {'trans': trans})

def select_language(request):
    if request.method == "POST":
        cur_language = translation.get_language()
        lang = request.POST['language']
        translation.activate(lang)
        return redirect('/'+lang)

def demo(request):
    return render(request, 'all_users.html')

