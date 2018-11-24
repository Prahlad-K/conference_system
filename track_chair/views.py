from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse
# Create your views here.

from conference_manager.models import Track


def index(request):
    tracks = Track.objects.filter(track_chair=request.user)

    total_tracks = len(tracks)
    
    submitted_tracks = Track.objects.filter(track_chair = request.user, paper_submitted= True)
    no_submitted_tracks = len(submitted_tracks)

    reviewed_tracks = Track.objects.filter(track_chair = request.user, report_submitted= True)
    no_reviewed_tracks = len(reviewed_tracks)

    tracks_under_permission = Track.objects.filter(track_chair = request.user, permission_requested= True)
    no_tracks_under_permission = len(tracks_under_permission)

    approved_tracks = Track.objects.filter(track_chair = request.user, track_approved= True)
    no_approved_tracks = len(approved_tracks)

    return render(request, 'track_chair/index.html', {'tracks':tracks, 'total_tracks':total_tracks, 'no_submitted_tracks':no_submitted_tracks, 'no_reviewed_tracks':no_reviewed_tracks, 'no_tracks_under_permission':no_tracks_under_permission, 'no_approved_tracks':no_approved_tracks})

def approve(request, track_id):
    track = Track.objects.get(pk = track_id)
    track.report_submitted = False
    track.permission_requested = True
    track.save()
    tracks = Track.objects.filter(track_chair=request.user)
    total_tracks = len(tracks)

    reviewed_tracks = Track.objects.filter(track_chair = request.user, report_submitted= True)
    no_reviewed_tracks = len(reviewed_tracks)

    tracks_under_permission = Track.objects.filter(track_chair = request.user, permission_requested= True)
    no_tracks_under_permission = len(tracks_under_permission)

    approved_tracks = Track.objects.filter(track_chair = request.user, track_approved= True)
    no_approved_tracks = len(approved_tracks)

    return render(request, 'track_chair/index.html', {'tracks':tracks, 'total_tracks':total_tracks, 'no_reviewed_tracks':no_reviewed_tracks, 'no_tracks_under_permission':no_tracks_under_permission, 'no_approved_tracks':no_approved_tracks})


def show_report(request, track_id):
    track = Track.objects.get(pk = track_id)
    print(track)
    return render(request, 'track_chair/show_report.html', {'track':track})

def revert_permission(request, track_id):
    track = Track.objects.get(pk = track_id)
    track.report_submitted = True
    track.permission_requested = False
    track.save()
    tracks = Track.objects.filter(track_chair=request.user)
    total_tracks = len(tracks)

    reviewed_tracks = Track.objects.filter(track_chair = request.user, report_submitted= True)
    no_reviewed_tracks = len(reviewed_tracks)

    tracks_under_permission = Track.objects.filter(track_chair = request.user, permission_requested= True)
    no_tracks_under_permission = len(tracks_under_permission)

    approved_tracks = Track.objects.filter(track_chair = request.user, track_approved= True)
    no_approved_tracks = len(approved_tracks)

    return render(request, 'track_chair/index.html', {'tracks':tracks, 'total_tracks':total_tracks, 'no_reviewed_tracks':no_reviewed_tracks, 'no_tracks_under_permission':no_tracks_under_permission, 'no_approved_tracks':no_approved_tracks})


def redo_report(request, track_id):
    track = Track.objects.get(pk = track_id)
    track.paper_submitted = True
    track.report_submitted = False
    
    track.save()
    tracks = Track.objects.filter(track_chair=request.user)
    total_tracks = len(tracks)

    reviewed_tracks = Track.objects.filter(track_chair = request.user, report_submitted= True)
    no_reviewed_tracks = len(reviewed_tracks)

    tracks_under_permission = Track.objects.filter(track_chair = request.user, permission_requested= True)
    no_tracks_under_permission = len(tracks_under_permission)

    approved_tracks = Track.objects.filter(track_chair = request.user, track_approved= True)
    no_approved_tracks = len(approved_tracks)

    return render(request, 'track_chair/index.html', {'tracks':tracks, 'total_tracks':total_tracks, 'no_reviewed_tracks':no_reviewed_tracks, 'no_tracks_under_permission':no_tracks_under_permission, 'no_approved_tracks':no_approved_tracks})

