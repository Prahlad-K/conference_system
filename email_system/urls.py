# sendemail/urls.py
from django.contrib import admin
from django.urls import path
from .views import *
#app_name='sendemail'

urlpatterns = [
    path('drafts/',display_draft,name='display'),
    path('customise/<int:pk>/',edit_draft,name='edit_draft'),
    
]
