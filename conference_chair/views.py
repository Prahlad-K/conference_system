from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse
# Create your views here.

from conference_manager.models import Track


def index(request):
    tracks = Track.objects.all()

    return render(request, 'conference_chair/index.html', {'tracks':tracks})