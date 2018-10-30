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

#Create your views here.

def index(request):
    tracks = Track.objects.filter(author=request.user)

    if request.method == 'POST':
        form = AdPaperForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            m = form.instance
            track = Track()
            track.author = request.user
            revs = CustomUser.objects.filter(roles = Role.objects.get(id=2))
            for rev in revs:
                if not rev.is_superuser:
                    track.reviewer=rev
                    break
            trcs = CustomUser.objects.filter(roles = Role.objects.get(id=3))
            for trc in trcs:
                if not trc.is_superuser:
                    track.track_chair=trc
                    break

            track.paper = m
            track.save()
            messages.info(request, 'Your response has been recorded successfully!')
        return render(request,'author/index.html',{'form':AdPaperForm,'tracks':tracks})
    
    return render(request,'author/index.html',{'form':AdPaperForm,'tracks':tracks})