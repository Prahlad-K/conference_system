from django.urls import path
from django.conf.urls import include, url  
from . import views
from .views import index

app_name = 'author'

urlpatterns=[
     url('index', views.index,name="index"),
]