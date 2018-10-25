from django.urls import path
from django.conf.urls import include, url  
from . import views
from .views import PostAdPage

app_name = 'author'

urlpatterns=[
     url('', PostAdPage.as_view()),
]