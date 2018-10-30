from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse
# Create your views here.

from conference_manager.models import Track


def index(request):
    tracks = Track.objects.filter(track_chair=request.user)

    return render(request, 'track_chair/index.html', {'tracks':tracks})

def approve(request, track_id):
    track = Track.objects.get(pk = track_id)
    track.report_submitted = False
    track.report_approved = True
    track.save()
    tracks = Track.objects.filter(track_chair=request.user)
    return render(request, 'track_chair/index.html', {'tracks':tracks})