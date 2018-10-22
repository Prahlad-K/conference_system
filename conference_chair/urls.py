from django.urls import path
from . import views

app_name = 'conference_chair'

urlpatterns = [
    path('', views.index, name='index')
]