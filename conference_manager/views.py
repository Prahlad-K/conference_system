from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import *
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    return render(request, 'conference_manager/index.html', {})

def create_track(request):
    if request.method == "GET":
        authors = CustomUser.objects.filter(roles__id = 1)
        reviewers = CustomUser.objects.filter(roles__id = 2)
        track_chairs = CustomUser.objects.filter(roles__id = 3)
        print(authors, reviewers, track_chairs)
        response = {}
        response['authors'] = authors
        response['reviewers'] = reviewers
        response['track_chairs'] = track_chairs

        return render(request, 'conference_manager/create_track.html', response)
    elif request.method == "POST":
        author = CustomUser.objects.get(username = request.POST['author'])
        reviewer = CustomUser.objects.get(username = request.POST['reviewer'])
        track_chair = CustomUser.objects.get(username = request.POST['track_chair'])
        track = Track.objects.create(author = author, reviewer = reviewer, track_chair = track_chair)
        print(track)
        return render(request, 'conference_manager/create_track.html', {})

def view_tracks(request):
    return render(request, 'conference_manager/view_tracks.html', {})

def add_user(request):
    if request.method == "GET":
        roles = Role.objects.all()
        response = {}
        response['roles'] = roles
        return render(request, 'conference_manager/add_user.html', response)
    elif request.method == "POST":
        print(request.POST)
        u = CustomUser.objects.create(username=request.POST['username'], password=request.POST['password'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'])
        u.roles.add(Role.objects.get(id = request.POST['role']))
        return render(request, 'conference_manager/add_user.html', {})

def view_users(request):
    return render(request, 'conference_manager/view_users.html', {})