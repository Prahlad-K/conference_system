from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import *
from django.http import HttpResponse
from .models import *
from email_system import urls
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
        track = Track.objects.create(author = author, reviewer = reviewer, track_chair = track_chair, description = request.POST['description'])
        authors = CustomUser.objects.filter(roles__id = 1)
        reviewers = CustomUser.objects.filter(roles__id = 2)
        track_chairs = CustomUser.objects.filter(roles__id = 3)
        print(track)
        response = {
            'success': True,
            'authors': authors,
            'reviewers': reviewers,
            'track_chairs': track_chairs,
        }
        return render(request, 'conference_manager/create_track.html', response)

def view_tracks(request):
    tracks = Track.objects.all()
    response = {}
    response['tracks'] = tracks
    return render(request, 'conference_manager/view_tracks.html', response)

def add_user(request):
    if request.method == "GET":
        roles = Role.objects.all()
        response = {}
        response['roles'] = roles
        return render(request, 'conference_manager/add_user.html', response)
    elif request.method == "POST":
        print(request.POST)
        u = CustomUser.objects.create(username=request.POST['username'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'])
        u.set_password(request.POST['password'])
        u.save()
        u.roles.add(Role.objects.get(id = request.POST['role']))
        roles = Role.objects.all()
        response = {
            'success': True,
            'roles': roles
        }
        return render(request, 'conference_manager/add_user.html', response)

def view_users(request):
    users = CustomUser.objects.all()
    for user in users:
        user.r = user.roles.all()
        print(user.r)
    response = {}
    response['users'] = users
    print(users)
    return render(request, 'conference_manager/view_users.html', response)

def view_user(request, username):
    if request.method == "GET":
        try:
            user = CustomUser.objects.get(username=username)
            user.r = user.roles.all()
            all_roles = Role.objects.all()
            not_assigned_roles = []
            for role in all_roles:
                if role not in user.r:
                    not_assigned_roles.append(role)
            print(not_assigned_roles)
            response = {}
            response['user'] = user
            response['not_assigned_roles'] = not_assigned_roles
            return render(request, 'conference_manager/view_user.html', response)
        except:
            return view_users(request)

    elif request.method == "POST":
        try:
            print(request.POST)
            user = CustomUser.objects.get(username=username)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.username = request.POST['username']
            user.roles.clear()
            try:
                value = request.POST['Author']
                user.roles.add(Role.objects.get(id=1))
            except:
                pass
            try:
                value = request.POST['Reviewer']
                user.roles.add(Role.objects.get(id=2))
            except:
                pass
            try:
                value = request.POST['Track Chair']
                user.roles.add(Role.objects.get(id=3))
            except:
                pass
            try:
                value = request.POST['Conference Chair']
                user.roles.add(Role.objects.get(id=4))
            except:
                pass
            try:
                value = request.POST['Registration Manager']
                user.roles.add(Role.objects.get(id=5))
            except:
                pass
            try:
                value = request.POST['Conference Manager']
                user.roles.add(Role.objects.get(id=6))
            except:
                pass
            user.save()
            user.r = user.roles.all()
            all_roles = Role.objects.all()
            not_assigned_roles = []
            for role in all_roles:
                if role not in user.r:
                    not_assigned_roles.append(role)
            response = {}
            response['user'] = user
            response['not_assigned_roles'] = not_assigned_roles
            response['success'] = True
            return render(request, 'conference_manager/view_user.html', response)
        except:
            return view_users(request)

def view_track(request, pk):
    if request.method == "GET":
        track = Track.objects.get(pk = pk)
        authors = CustomUser.objects.filter(roles__id = 1)
        reviewers = CustomUser.objects.filter(roles__id = 2)
        track_chairs = CustomUser.objects.filter(roles__id = 3)
        response = {
            'track': track,
            'authors': authors,
            'reviewers': reviewers,
            'track_chairs': track_chairs
        }
        return render(request, 'conference_manager/view_track.html', response)
    elif request.method == "POST":
        print(request.POST)
        track = Track.objects.get(pk = pk)
        track.author = CustomUser.objects.get(username=request.POST['author'])
        track.reviewer = CustomUser.objects.get(username=request.POST['reviewer'])
        track.track_chair = CustomUser.objects.get(username=request.POST['track_chair'])
        track.description = request.POST['description']
        track.save()
        authors = CustomUser.objects.filter(roles__id = 1)
        reviewers = CustomUser.objects.filter(roles__id = 2)
        track_chairs = CustomUser.objects.filter(roles__id = 3)
        response = {
            'track': track,
            'authors': authors,
            'reviewers': reviewers,
            'track_chairs': track_chairs,
            'success': True
        }
        return render(request, 'conference_manager/view_track.html', response)

def delete_track(request, pk):
    try:
        Track.objects.get(pk=pk).delete()
        return view_tracks(request)
    except:
        return view_tracks(request)

def delete_user(request, pk):
    try:
        CustomUser.objects.get(pk=pk).delete()
        return view_users(request)
    except:
        return view_users(request)
