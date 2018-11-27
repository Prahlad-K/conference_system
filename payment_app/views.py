from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse,BadHeaderError
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
import sys
import datetime

from payment_app.forms import collectPaymentForm, ContactForm

from payment_app.models import Payment
from email_system.models import draft

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
                
                subject="Thanks!"
                o=draft.objects.get(title="Payment")
                message=o.text
                to_email=request.user.email
                username=payment.user
                to_email="myusernameanusha@gmail.com"
                ctx={
                'username': username,
                'message_body': message
                }
                try:
                    send_mail(subject, get_template('templates_path/pay_email.html').render(ctx), 'anush.meh@gmail.com', [to_email])
                except:
                    print("Send mail failed")
                    return render(request,'payment_app/error.html')
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

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            to_email = form.cleaned_data['email_id']
            message = form.cleaned_data['message']
            print(to_email)
            print(subject)
            print(message)
            try:
                send_mail(subject, message, 'anush.meh@gmail.com', [to_email])
            except:
                print("Error:",sys.exc_info()[0])
                return render(request,'payment_app/error.html')
            return redirect('http://127.0.0.1:8000/payment_app/thankyou')
    if request.method=='GET':
        form=ContactForm()
    return render(request, "payment_app/contact.html",{'form':form})
def thankyou(request):
    return render(request,"payment_app/thankyou.html")