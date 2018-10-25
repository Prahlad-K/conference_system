from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse
from django.views.generic import FormView
from .models import ResearchPaper 
from .forms import AdPaperForm
from conference_manager.models import Track
from payment_app.models import Payment

#Create your views here.

def index(request):
    if request.method == 'POST':
        form = AdPaperForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'author/index.html',{'form':AdPaperForm})
    else:
        return render(request,'author/index.html',{'form':AdPaperForm})        