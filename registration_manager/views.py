from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse
import datetime

from registration_manager.forms import collectPaymentForm

from registration_manager.models import Payment

# Create your views here.

def display(request):
    payments = Payment.objects.all()
    return render(request, 'registration_manager/display.html', {'payments':payments})

def index(request):
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
            return render(request, 'registration_manager/status.html', {'payment':payment})

    return render(request, 'registration_manager/index.html')

def wait(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    payment.ongoing = True
    payment.started = False
    payment.save()
    return render(request, 'registration_manager/status.html', {'payment':payment})

def approve(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    payment.ongoing = False
    payment.approved = True
    payment.save()
    return render(request, 'registration_manager/status.html', {'payment':payment})

def complete(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    payment.approved = False
    payment.completed = True
    payment.save()
    return render(request, 'registration_manager/status.html', {'payment':payment})

def status(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)

    return render(request, 'registration_manager/status.html', {'payment':payment})

def delete(request, payment_id):
    Payment.objects.get(id=payment_id).delete()
    print(payment_id)
    return render(request, 'registration_manager/display.html')