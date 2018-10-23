from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from payment.forms import collectPaymentForm

from payment.models import Payment

# Create your views here.
def index(request):
    payment = Payment()
    payment_id = payment.id
    if request.method == 'POST':
        credit_card_form = collectPaymentForm(request.POST)

        if credit_card_form.is_valid():
            payment.credit_card_no = credit_card_form.cleaned_data['credit_card_no']
            payment.amount = credit_card_form.cleaned_data['amount']
            payment.user_details = credit_card_form.cleaned_data['user_details']
            payment.payment_date = credit_card_form.cleaned_data['payment_date']
            payment.started = True
            payment.save()
            return render(request, 'payment/status.html', {'payment':payment})

    return render(request, 'payment/index.html')

def status(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)

    return render(request, 'payment/status.html', {'payment':payment})

def approve(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    payment.started = False
    payment.approved = True

    return render(request, 'payment/status.html', {'payment':payment})