from django.shortcuts import render

# Create your views here.
urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in', views.sign_in, name='sign_in'),
]