from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
# Create your views here.

def index(request):
    print("Index")
    if request.user.is_authenticated and request.user.is_active == True:
        print("Already authenticated")
        return choose_profile(request, request.user)
    else:
        print("Needs authentication")
        response = {}
        return render(request, 'authentication/login.html', {})

def choose_profile(request, user):
    response = {}
    roles = request.user.roles.all()
    response['roles'] = roles
    print(roles)
    return render(request, 'authentication/choose_profile.html', response)

def sign_in(request): 
    print("Sign in request")
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        if user is None:
            return render(request,'authentication/login.html',{'error':'Invalid username or password'})
        else:
            login(request, user)
            print("Log in successful")
            return choose_profile(request, user)
    else:
        return index(request)