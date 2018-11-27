from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from conference_manager.models import Track, Conference
from .models import *
from django.core.mail import send_mail, BadHeaderError
from email_system.models import draft
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def index(request):
    print("Index")
    if request.user.is_authenticated and request.user.is_active == True:
        print("Already authenticated")
        return choose_profile(request, request.user)
    else:
        print("Needs authentication")
        
        return render(request, 'authentication/login_page.html', {})

def choose_profile(request, user):
    response = {}
    roles = request.user.roles.all()
    response['roles'] = roles
    print(roles)
    conferences = Conference.objects.all()
    superuser = False
    if len(conferences)==0:
        if user.is_superuser:
            superuser= True
        return render(request, 'authentication/error_page.html', {'superuser':superuser})
    else:
        manager = CustomUser.objects.get(roles = Role.objects.get(id = 6))
        conference = Conference.objects.get(conference_manager = manager)
        response['conference'] = conference
        return render(request, 'authentication/main_page.html', response)

def sign_in(request): 
    print("Sign in request")
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is None:
            return render(request,'authentication/login_page.html',{'error':'Invalid username or password'})
        elif user.validated is False:
            return render(request,'authentication/login_page.html',{'error':'Your signup is not yet approved'})
        else:
            login(request, user)
            print("Log in successful")
            return choose_profile(request, user)
    else:
        return index(request)

def logout_view(request):
    logout(request)
    return sign_in(request)  

def sign_up(request):
    if request.method == "GET":
        roles = Role.objects.all()
        response = {}
        response['roles'] = roles
        return render(request, 'authentication/sign_up.html', response)
    elif request.method == "POST":
        print(request.POST)
        u = CustomUser.objects.create(username=request.POST['username'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'])
        u.set_password(request.POST['password'])
        
        try:
            value = request.POST['Author']
            u.roles.add(Role.objects.get(id=1))
        except:
            pass
        try:
            value = request.POST['Reviewer']
            u.roles.add(Role.objects.get(id=2))
        except:
            pass
        try:
            value = request.POST['Track Chair']
            u.roles.add(Role.objects.get(id=3))
        except:
            pass
        try:
            value = request.POST['Conference Chair']
            u.roles.add(Role.objects.get(id=4))
        except:
            pass
        try:
            value = request.POST['Registration Manager']
            u.roles.add(Role.objects.get(id=5))
        except:
            pass
        try:
            value = request.POST['Conference Manager']
            u.roles.add(Role.objects.get(id=6))
        except:
            pass
        
        roles = Role.objects.all()
        subject="Thank you for signing up with us!"
        o=draft.objects.get(title="Registration")
        message=o.text
        to_email=u.email
        username=u.username
        u.save()
        ctx={
        'username': username,
        'message_body': message
        }
        try:
            send_mail(subject, get_template('templates_path/reg_email.html').render(ctx), 'prahladsharmak99@gmail.com', [to_email])
        except:
            print("Send mail failed")
        response = {
            'success': True,
            'roles': roles
        }
        return render(request, 'authentication/validation_page.html')
