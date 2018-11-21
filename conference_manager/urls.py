from django.urls import path
from . import views

app_name = 'conference_manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_conference', views.create_conference, name='create_conference'),
    path('view_conferences', views.view_conferences, name='view_conferences'),
    path('create_track', views.create_track, name='create_track'),
    path('view_tracks', views.view_tracks, name='view_tracks'),
    path('add_user', views.add_user, name='add_user'),
    path('view_users', views.view_users, name='view_users'),
    path('view_user/<slug:username>', views.view_user, name='view_user'),
    path('view_track/<int:pk>', views.view_track, name='view_track'),
    path('view_conference/<int:pk>', views.view_conference, name='view_conference'),
    path('delete_track/<int:pk>', views.delete_track, name='delete_track'),
    path('delete_user/<int:pk>', views.delete_user, name='delete_user'),
    path('delete_conference/<int:pk>', views.delete_conference, name='delete_conference'),
]