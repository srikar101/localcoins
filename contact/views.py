import email
from email import message
from django.shortcuts import redirect, render

from contact.models import Contact

# Create your views here.

def contact(request):
    return render(request, 'contact.html')

def post_contact(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        k = Contact(username=username,email=email,subject=subject,message=message)
        k.save()
        return redirect('home')
    return redirect('home/contact')
