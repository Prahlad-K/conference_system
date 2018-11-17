from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse
# Create your views here.

from .models import ReviewReport  
from .forms import ReviewForm
from conference_manager.models import Track


def index(request):
    tracks = Track.objects.filter(reviewer=request.user)
    reports = ReviewReport.objects.all()
    
    total_tracks =  len(tracks)

    reviewed_tracks = Track.objects.filter(reviewer = request.user, report_submitted= True)
    no_reviewed_tracks = len(reviewed_tracks)

    tracks_under_permission = Track.objects.filter(reviewer = request.user, permission_requested= True)
    no_tracks_under_permission = len(tracks_under_permission)

    approved_tracks = Track.objects.filter(reviewer = request.user, track_approved= True)
    no_approved_tracks = len(approved_tracks)

    return render(request, 'reviewer/index.html', {'tracks':tracks, 'reports':reports, 'no_reviewed_tracks': no_reviewed_tracks, 'no_tracks_under_permission':no_tracks_under_permission, 'total_tracks':total_tracks, 'no_approved_tracks':no_approved_tracks})


def submit(request, track_id):
    track = Track.objects.get(pk = track_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():        
            track.report = form.instance 
            track.paper_submitted = False   
            track.report_submitted = True
            form.save()
            track.save()
            return render(request, 'reviewer/report.html', {'form':ReviewForm})
    return render(request, 'reviewer/report.html', {'form':ReviewForm})