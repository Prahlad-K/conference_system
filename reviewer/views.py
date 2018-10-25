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
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'reviewer/index.html', {'form':ReviewForm, 'tracks':tracks, 'reports':reports})
    return render(request, 'reviewer/index.html', {'form':ReviewForm, 'tracks':tracks, 'reports':reports})
