from email import message
from django.shortcuts import redirect, render

from account.models import Register
import support

from support.models import Support

# Create your views here.

def post_support_tickets(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        priority = request.POST['priority']
        message = request.POST['message']
        attachments = request.FILES.get('attachments')
        k = Support(support_name=name,email=email,subject=subject,priority=priority,message=message,attachments=attachments)
        k.save()
        return redirect('user_auth')
    return render(request, 'supportticket.html')

def get_my_support_tickets(request):
    username = request.session['username']
    post = Support.objects.filter(support_name=username)
    return render(request, 'mysupportticket.html', {'post': post})

    