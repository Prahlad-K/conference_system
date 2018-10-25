from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import get_object_or_404, render, redirect
from authentication.models import CustomUser
from django.http import HttpResponse
from django.views.generic import FormView
# Create your views here.

def index(request):
    return HttpResponse("<p>Author</p>")

from .models import PostAd  
from .forms import PostAdForm

class PostAdPage(FormView):  
    template_name = 'author/index.html'
    success_url = '/awesome/'
    form_class = PostAdForm

    def form_valid(self, form):
        return HttpResponse("Sweeeeeet.")