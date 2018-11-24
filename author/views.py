from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser,Role
from django.http import HttpResponse
from django.views.generic import FormView
from .models import ResearchPaper 
from .forms import AdPaperForm
from conference_manager.models import Track, Conference
from payment_app.models import Payment
from django.contrib import messages
from django.http import HttpResponseRedirect

import random
import datetime

#Create your views here.
from .models import ResearchPaper

def index(request):
    tracks = Track.objects.filter(author=request.user)
    total_tracks = len(tracks)

    submitted_tracks = Track.objects.filter(author = request.user, paper_submitted= True)
    no_submitted_tracks = len(submitted_tracks)

    reviewed_tracks = Track.objects.filter(author = request.user, report_submitted= True)
    no_reviewed_tracks = len(reviewed_tracks)

    tracks_under_permission = Track.objects.filter(reviewer = request.user, permission_requested= True)
    no_tracks_under_permission = len(tracks_under_permission)

    approved_tracks = Track.objects.filter(author = request.user, track_approved= True)
    no_approved_tracks = len(approved_tracks)

    for track in tracks:
        print(track.paper.submission_date)
        dt =  datetime.date.today()- track.paper.submission_date
        track.paper.days_left = 7 - dt.days

    paid = False
    payments = Payment.objects.filter(completed = True)
    for payment in payments:
        if payment.user ==request.user:
            paid = True
    
    if not paid:
        manager = CustomUser.objects.get(roles = Role.objects.get(id = 6), is_superuser = False)
        conference = Conference.objects.get(conference_manager = manager)
        response = {}
        response['conference'] = conference
        return render(request, 'author/payfee.html', response)
            

    if request.method == 'POST':
        form = AdPaperForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            m = form.instance
            track = Track()
            track.author = request.user
            revs = CustomUser.objects.filter(roles = Role.objects.get(id=2), is_superuser = False)
           #selects random reviewer
            print(revs)

            index = random.randint(0,len(revs)-1)
            track.reviewer = revs[index]

            trcs = CustomUser.objects.filter(roles = Role.objects.get(id=3), is_superuser = False)
           #selects random track chair
            print(trcs)

            index = random.randint(0,len(trcs)-1)
            track.track_chair = trcs[index]
            
            track.paper = m
            track.paper_submitted = True
            track.save()
            messages.info(request, 'Your response has been recorded successfully!')
            tracks = Track.objects.filter(author=request.user)
            total_tracks = len(tracks)

            submitted_tracks = Track.objects.filter(author = request.user, paper_submitted= True)
            no_submitted_tracks = len(submitted_tracks)

            reviewed_tracks = Track.objects.filter(author = request.user, report_submitted= True)
            no_reviewed_tracks = len(reviewed_tracks)

            tracks_under_permission = Track.objects.filter(reviewer = request.user, permission_requested= True)
            no_tracks_under_permission = len(tracks_under_permission)

            approved_tracks = Track.objects.filter(author = request.user, track_approved= True)
            no_approved_tracks = len(approved_tracks)

            for track in tracks:
                print(track.paper.submission_date)
                dt =  datetime.date.today()- track.paper.submission_date
                track.paper.days_left = 7 - dt.days

            return render(request,'author/index.html',{'form':AdPaperForm,'tracks':tracks, 'no_submitted_tracks':no_submitted_tracks, 'no_reviewed_tracks':no_reviewed_tracks, 'no_approved_tracks':no_approved_tracks, 'total_tracks':total_tracks, 'no_tracks_under_permission':no_tracks_under_permission})
    
    return render(request,'author/index.html',{'form':AdPaperForm,'tracks':tracks, 'no_submitted_tracks':no_submitted_tracks, 'no_reviewed_tracks':no_reviewed_tracks, 'no_approved_tracks':no_approved_tracks, 'total_tracks':total_tracks, 'no_tracks_under_permission':no_tracks_under_permission})

def edit(request,track_id):
    tracks = Track.objects.filter(author=request.user)
    total_tracks = len(tracks)

    submitted_tracks = Track.objects.filter(author = request.user, paper_submitted= True)
    no_submitted_tracks = len(submitted_tracks)

    reviewed_tracks = Track.objects.filter(author = request.user, report_submitted= True)
    no_reviewed_tracks = len(reviewed_tracks)

    tracks_under_permission = Track.objects.filter(reviewer = request.user, permission_requested= True)
    no_tracks_under_permission = len(tracks_under_permission)

    approved_tracks = Track.objects.filter(author = request.user, track_approved= True)
    no_approved_tracks = len(approved_tracks)

    if request.method == 'POST':
        ins = Track.objects.get(id=track_id)
        paper = ins.paper
        form = AdPaperForm(request.POST,request.FILES,instance=paper)
        print(1)
        if form.is_valid():
            print(2)
            form.save()
            m = form.instance
            track = Track.objects.get(id=track_id)
            track.paper = m
            track.paper_submitted = True
            track.description = paper.title
            track.save()
            messages.info(request, 'Your response has been recorded successfully!')
            tracks = Track.objects.filter(author=request.user)
            total_tracks = len(tracks)

            submitted_tracks = Track.objects.filter(author = request.user, paper_submitted= True)
            no_submitted_tracks = len(submitted_tracks)

            reviewed_tracks = Track.objects.filter(author = request.user, report_submitted= True)
            no_reviewed_tracks = len(reviewed_tracks)

            tracks_under_permission = Track.objects.filter(reviewer = request.user, permission_requested= True)
            no_tracks_under_permission = len(tracks_under_permission)

            approved_tracks = Track.objects.filter(author = request.user, track_approved= True)
            no_approved_tracks = len(approved_tracks)
            return render(request,'author/index.html',{'form':AdPaperForm,'tracks':tracks, 'no_submitted_tracks':no_submitted_tracks, 'no_reviewed_tracks':no_reviewed_tracks, 'no_approved_tracks':no_approved_tracks, 'total_tracks':total_tracks, 'no_tracks_under_permission':no_tracks_under_permission})
        return render(request,'author/edit_submission.html',{'form':form,'track_id':track_id})    
    else:
        ins = Track.objects.get(id=track_id)
        paper = ins.paper
        myForm = AdPaperForm(instance=paper)
        return render(request,'author/edit_submission.html',{'form':myForm,'track_id':track_id})    