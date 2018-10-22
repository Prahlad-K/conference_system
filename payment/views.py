from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from payment.forms import collectPaymentForm

from payment.models import Payment

# Create your views here.
def index(request):
    list_of_payments = Payment.objects.order_by('-payment_date')[:5]
    context = {'list_of_payments' : list_of_payments}
    return render(request, 'payment/index.html', context)

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
