from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse
import datetime

from payment_app.models import Payment

# Create your views here.

def display(request):
    payments = Payment.objects.all()
    roles = request.user.roles.all()
    return render(request, 'registration_manager/display.html', {'payments':payments, 'roles':roles})

def approve(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    payment.ongoing = False
    payment.approved = True
    payment.save()
    payments = Payment.objects.all()
    roles = request.user.roles.all()
    return render(request, 'registration_manager/display.html',  {'payments':payments, 'roles':roles})

def delete(request, payment_id):
    Payment.objects.get(id=payment_id).delete()
    print(payment_id)
    payments = Payment.objects.all()
    roles = request.user.roles.all()
    return render(request, 'registration_manager/display.html',  {'payments':payments, 'roles':roles})