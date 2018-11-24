from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages
from conference_manager.models import Track


def index(request):
    tracks = Track.objects.all()
    
    total_tracks = len(tracks)

    tracks_under_permission = Track.objects.filter(permission_requested= True)
    no_tracks_under_permission = len(tracks_under_permission)

    approved_tracks = Track.objects.filter(track_approved= True)
    no_approved_tracks = len(approved_tracks)

    if no_approved_tracks == total_tracks:
        messages.info(request, "All tracks have been approved!")
    
    other_tracks = total_tracks - no_approved_tracks - no_tracks_under_permission

    return render(request, 'conference_chair/index.html', {'tracks':tracks, 'total_tracks':total_tracks, 'other_tracks':other_tracks, 'no_tracks_under_permission':no_tracks_under_permission, 'no_approved_tracks':no_approved_tracks})

def show_report(request, track_id):
    track = Track.objects.get(pk = track_id)
    print(track)
    return render(request, 'conference_chair/show_report.html', {'track':track})

def give_permission(request, track_id):
    track = Track.objects.get(pk = track_id)

    track.track_approved = True
    track.permission_requested = False

    track.save()
    tracks = Track.objects.all()
    
    total_tracks = len(tracks)

    tracks_under_permission = Track.objects.filter(permission_requested= True)
    no_tracks_under_permission = len(tracks_under_permission)

    approved_tracks = Track.objects.filter(track_approved= True)
    no_approved_tracks = len(approved_tracks)

    if no_approved_tracks == total_tracks:
        messages.info(request, "All tracks have been approved!")

    
    other_tracks = total_tracks - no_approved_tracks - no_tracks_under_permission

    return render(request, 'conference_chair/index.html', {'tracks':tracks, 'total_tracks':total_tracks, 'other_tracks':other_tracks, 'no_tracks_under_permission':no_tracks_under_permission, 'no_approved_tracks':no_approved_tracks})

def reject_permission(request, track_id):
    track = Track.objects.get(pk = track_id)

    track.track_approved = False
    track.permission_requested = True

    track.save()

    tracks = Track.objects.all()
    
    total_tracks = len(tracks)

    tracks_under_permission = Track.objects.filter(permission_requested= True)
    no_tracks_under_permission = len(tracks_under_permission)

    approved_tracks = Track.objects.filter(track_approved= True)
    no_approved_tracks = len(approved_tracks)

    if no_approved_tracks == total_tracks:
        messages.info(request, "All tracks have been approved!")
    
    other_tracks = total_tracks - no_approved_tracks - no_tracks_under_permission

    return render(request, 'conference_chair/index.html', {'tracks':tracks, 'total_tracks':total_tracks, 'other_tracks':other_tracks, 'no_tracks_under_permission':no_tracks_under_permission, 'no_approved_tracks':no_approved_tracks})

