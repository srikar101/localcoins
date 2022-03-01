from django.shortcuts import render

from policypages_managesection.models import ManageSection, PolicyPages

# Create your views here.

def manage_section(request):
    post = ManageSection.objects.all()
    return render(request, 'managesection.html', {'post': post})


def policy_pages(request):
    post = PolicyPages.objects.all()
    return render(request, 'policypages.html', {'post': post})