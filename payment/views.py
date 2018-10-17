from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from payment.models import Payment

# Create your views here.
def index(request):
    list_of_payments = Payment.objects.order_by('-payment_date')[:5]
    context = {'list_of_payments' : list_of_payments}
    return render(request, 'payment/index.html', context)

def detail(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    return render(request, 'payment/detail.html', {'payment':payment})

def start(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    return render(request, 'payment/start.html', {'payment':payment})

def status(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    return render(request, 'payment/status.html', {'payment':payment})