from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser,Role
from django.http import HttpResponse
from django.views.generic import FormView
from .models import ResearchPaper 
from .forms import AdPaperForm
from conference_manager.models import Track
from payment_app.models import Payment
from django.contrib import messages
from django.http import HttpResponseRedirect

import random

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

    if request.method == 'POST':
        form = AdPaperForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            m = form.instance
            track = Track()
            track.author = request.user
            revs = CustomUser.objects.filter(roles = Role.objects.get(id=2), is_superuser = False)
           #selects random reviewer
            index = random.randint(0,len(revs)-1)
            track.reviewer = revs[index]

            trcs = CustomUser.objects.filter(roles = Role.objects.get(id=3), is_superuser = False)
           #selects random track chair 
            index = random.randint(0,len(trcs)-1)
            
            track.track_chair = trcs[index]
            
            track.paper = m
            track.paper_submitted = True
            track.save()
            messages.info(request, 'Your response has been recorded successfully!')
        return render(request,'author/index.html',{'form':AdPaperForm,'tracks':tracks, 'no_submitted_tracks':no_submitted_tracks, 'no_reviewed_tracks':no_reviewed_tracks, 'no_approved_tracks':no_approved_tracks, 'total_tracks':total_tracks, 'no_tracks_under_permission':no_tracks_under_permission})
    
    return render(request,'author/index.html',{'form':AdPaperForm,'tracks':tracks, 'no_submitted_tracks':no_submitted_tracks, 'no_reviewed_tracks':no_reviewed_tracks, 'no_approved_tracks':no_approved_tracks, 'total_tracks':total_tracks, 'no_tracks_under_permission':no_tracks_under_permission})

def edit(request,track_paper_id):
    ins = ResearchPaper.objects.get(id=track_paper_id)
    myForm = AdPaperForm(instance=ins)
    return render(request,'author/edit_submission.html',{'form':myForm})    