from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse
import datetime

from payment_app.models import Payment
from conference_manager.models import CustomUser

# Create your views here.

def display(request):
    payments = Payment.objects.all()
    roles = request.user.roles.all()
    users = CustomUser.objects.all()
    return render(request, 'registration_manager/display.html', {'payments':payments, 'roles':roles,'users':users})

def approve(request, payment_id):
    payment = get_object_or_404(Payment, pk = payment_id)
    payment.ongoing = False
    payment.approved = True
    payment.save()
    payments = Payment.objects.all()
    roles = request.user.roles.all()
    users = CustomUser.objects.all()
    return render(request, 'registration_manager/display.html',  {'payments':payments, 'roles':roles, 'users':users})

def approve_user(request, user_id):
    user_ = get_object_or_404(CustomUser, pk = user_id)
    user_.validated=True
    user_.save()
    payments = Payment.objects.all()
    roles = request.user.roles.all()
    users = CustomUser.objects.all()
    return render(request, 'registration_manager/display.html',  {'payments':payments, 'roles':roles,'users':users})


def delete(request, payment_id):
    Payment.objects.get(id=payment_id).delete()
    print(payment_id)
    payments = Payment.objects.all()
    roles = request.user.roles.all()
    users = CustomUser.objects.all()
    return render(request, 'registration_manager/display.html',  {'payments':payments, 'roles':roles, 'users':users})