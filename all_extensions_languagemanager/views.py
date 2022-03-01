from email.policy import default
from re import L
from django.shortcuts import redirect, render

from all_extensions_languagemanager.models import Extension, LanguageManager

# Create your views here.

def get_extensions(request):
    post = Extension.objects.all()
    return render(request, 'extension.html', {'post': post})

def all_languages(request):
    post = LanguageManager.objects.all()
    return render(request, 'language.html', {'post': post})

def add_language(request):
    if request.method == "POST":
        name = request.POST['name']
        code = request.POST['code']
        default = request.POST['default']
        k = LanguageManager(language_name=name,code=code,default=default)
        k.save()
        return redirect('languagemanager')
    return render(request, 'addlanguage.html')

def edit_language(request,id):
    obj = LanguageManager.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        code = request.POST['code']
        default = request.POST['default']
        LanguageManager.objects.filter(id=id).update(language_name=name,code=code,default=default)
        return redirect('languagemanager')
    else:
        return render(request, 'edit_language.html', {'obj': obj})

def delete_language(request,id):
    obj = LanguageManager.objects.get(id=id)
    obj.delete()
    return redirect('languagemanager')

