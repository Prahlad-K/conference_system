from django.urls import path
from . import views

app_name = 'conference_manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_track', views.create_track, name='create_track'),
    path('view_tracks', views.create_track, name='view_tracks'),
    path('add_user', views.add_user, name='add_user'),
    path('view_users', views.view_users, name='view_users'),
    path('view_user/<slug:username>', views.view_user, name='view_user'),
]