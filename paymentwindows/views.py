from django.shortcuts import redirect, render

from paymentwindows.models import PaymentWindows

# Create your views here.

def payment_window(request):
    post = PaymentWindows.objects.all()
    return render(request, 'admin_paymentwindows.html',{'post': post})

def edit_window(request,id):
    obj = PaymentWindows.objects.get(id=id)
    if request.method == "POST":
        time = request.POST['time']
        print(obj.time)
        PaymentWindows.objects.filter(id=id).update(time=time)
        return redirect('paymentwindows')
    return render(request, 'edit_payment_window.html', {'obj': obj})

def delete_window(request, id):
    obj = PaymentWindows.objects.get(id=id)
    obj.delete()
    return redirect('paymentwindows')
    

    