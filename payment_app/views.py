from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse
import datetime

from payment_app.forms import collectPaymentForm

from payment_app.models import Payment

def index(request):

    try:
        payment = Payment.objects.get(user = request.user)
        return render(request, 'payment_app/status.html', {'payment':payment})
    except:
        payment = Payment()
        
        if request.method == 'POST':
            credit_card_form = collectPaymentForm(request.POST)

            if credit_card_form.is_valid():
                payment.credit_card_no = credit_card_form.cleaned_data['credit_card_no']
                payment.amount = credit_card_form.cleaned_data['amount']
                payment.cvv = credit_card_form.cleaned_data['cvv']
                payment.expiry_date = credit_card_form.cleaned_data['expiry_date']
                payment.user = request.user
                payment.payment_date = datetime.datetime.now()
                payment.started = True
                payment.save()
                return render(request, 'payment_app/status.html', {'payment':payment})
    return render(request, 'payment_app/index.html')
    

def wait(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    payment.ongoing = True
    payment.started = False
    payment.save()
    return render(request, 'payment_app/status.html', {'payment':payment})

def complete(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    payment.approved = True
    payment.completed = True
    payment.save()
    return render(request, 'payment_app/status.html', {'payment':payment})

def status(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)

    return render(request, 'payment_app/status.html', {'payment':payment})

