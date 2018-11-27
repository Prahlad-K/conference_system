# sendemail/urls.py
from django.contrib import admin
from django.urls import path
from . import views
#app_name='sendemail'
app_name = 'email_system'
urlpatterns = [
    path('drafts/',views.display_draft,name='display'),
    path('customise/<int:pk>/',views.edit_draft,name='edit_draft'),
    
]