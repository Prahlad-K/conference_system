from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from payment.forms import collectPaymentForm

from payment.models import Payment

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        credit_card_form = collectPaymentForm(request.POST)
        if credit_card_form.is_valid():
            payment = Payment()
            payment.credit_card_no = credit_card_form.cleaned_data['credit_card_no']
            payment.amount = credit_card_form.cleaned_data['amount']
            payment.paymentDetails = credit_card_form['paymentDetails']
            payment.payment_date = credit_card_form['payment_date']

            payment.save()
        #return HttpResponseRedirect(reverse('payment:status', args = (payment_id,)))

    return render(request, 'payment/index.html')

def detail(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    
    if request.method == 'POST':
        credit_card_form = collectPaymentForm(request.POST)
        if credit_card_form.is_valid():
            payment.credit_card_no = credit_card_form.cleaned_data['credit_card_no']
            payment.save()
        #return HttpResponseRedirect(reverse('payment:status', args = (payment_id,)))

    return render(request, 'payment/detail.html', {'payment':payment})

def start(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    started = True
    payment.save()
    return render(request, 'payment/start.html', {'payment':payment})

def status(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    return render(request, 'payment/status.html', {'payment':payment})

def approval(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    payment.started = False
    payment.approved = True
    payment.save()
    return HttpResponseRedirect(reverse('payment:status', args = (payment_id,)))
