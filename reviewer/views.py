from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

from .models import ReviewReport  
from .forms import ReviewForm
from conference_manager.models import Track
import datetime


def index(request):
    tracks = Track.objects.filter(reviewer=request.user)
    reports = ReviewReport.objects.all()
    
    total_tracks =  len(tracks)
    for track in tracks:
        dt =  datetime.date.today()- track.paper.submission_date
        track.paper.days_left = 7 - dt.days

    submitted_tracks = Track.objects.filter(reviewer = request.user, paper_submitted= True)
    no_submitted_tracks = len(submitted_tracks)

    reviewed_tracks = Track.objects.filter(reviewer = request.user, report_submitted= True)
    no_reviewed_tracks = len(reviewed_tracks)

    tracks_under_permission = Track.objects.filter(reviewer = request.user, permission_requested= True)
    no_tracks_under_permission = len(tracks_under_permission)

    approved_tracks = Track.objects.filter(reviewer = request.user, track_approved= True)
    no_approved_tracks = len(approved_tracks)

    return render(request, 'reviewer/index.html', {'tracks':tracks, 'reports':reports,'no_submitted_tracks':no_submitted_tracks, 'no_reviewed_tracks': no_reviewed_tracks, 'no_tracks_under_permission':no_tracks_under_permission, 'total_tracks':total_tracks, 'no_approved_tracks':no_approved_tracks})


def edit(request, track_id):
    track = Track.objects.get(pk = track_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():        
            form.save()
            m = form.instance
            track.report = m
            track.paper_submitted = False   
            track.report_submitted = True
            track.save()
            messages.info(request, 'Your response has been recorded successfully!')
            return render(request, 'reviewer/submit_report.html', {'form':form, 'track_id':track_id})
    else:
        report = track.report
        myForm = ReviewForm(instance=report)
        return render(request, 'reviewer/submit_report.html', {'form':myForm,'track_id':track_id})
