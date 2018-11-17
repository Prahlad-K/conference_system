from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from conference_manager.models import Track
from .models import *
# Create your views here.

def index(request):
    print("Index")
    if request.user.is_authenticated and request.user.is_active == True:
        print("Already authenticated")
        return choose_profile(request, request.user)
    else:
        print("Needs authentication")
        response = {}
        return render(request, 'authentication/login_page.html', {})

def choose_profile(request, user):
    response = {}
    roles = request.user.roles.all()
    response['roles'] = roles
    print(roles)
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
        u = CustomUser.objects.create(validated=False,username=request.POST['username'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'])
        u.set_password(request.POST['password'])
        u.save()
        u.roles.add(Role.objects.get(id = request.POST['role']))
        roles = Role.objects.all()
        return render(request, 'authentication/validation_page.html',{})
