from turtle import heading
from django.shortcuts import redirect, render

from emailtemplates_faq.models import FAQ, EmailTemplates

# Create your views here.

def email_templates(request):
    post = EmailTemplates.objects.all()
    return render(request, 'emailtemplates.html', {'post': post})

def get_FAQ(request):
    post = FAQ.objects.all()
    return render(request, 'faq.html', {'post': post})


def add_faq(request):
    if request.method == "POST":
        heading = request.POST['heading']
        sub_heading = request.POST['sub heading']
        k = FAQ(heading=heading,sub_heading=sub_heading)
        k.save()
        return redirect('faq')
    return render(request, 'addfaq.html')

def delete_faq(request,id):
    obj = FAQ.objects.get(id=id)
    obj.delete()
    return redirect('faq')

def edit_faq(request,id):
    obj = FAQ.objects.get(id=id)
    if request.method == "POST":
        heading = request.POST['heading']
        sub_heading = request.POST['sub heading']
        FAQ.objects.filter(id=id).update(heading=heading,sub_heading=sub_heading)
        return redirect('faq')
    return render(request, 'edit_faq.html', {'obj': obj})

