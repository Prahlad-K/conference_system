from django.urls import path
from . import views

app_name = 'reviewer'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:track_id>/edit', views.edit, name='edit'),
]