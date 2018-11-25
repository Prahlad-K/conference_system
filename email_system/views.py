from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from django.conf import settings
from .models import draft
from .forms import DraftForm
from .urls import *
from django.template import Context
from django.template.loader import get_template

app_name='email_system'

def display_draft(request):
    return render(request,"email_system/draft_templates.html")

def edit_draft(request,pk):
    data=get_object_or_404(draft,pk=pk)
    
    if request.method=="POST":
            form=DraftForm(request.POST,instance=data)
            if form.is_valid():
                data=form.save(commit=False)
                data.save()
            else:
                print("Form not valid")
    else:
        form= DraftForm(instance=data)
    return render(request,'email_system/edit_draft.html',{'form':form})
