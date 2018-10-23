from django.urls import path
from . import views

app_name = 'track_chair'

urlpatterns = [
    path('', views.index, name='index')
]