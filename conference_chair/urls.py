from django.urls import path
from . import views

app_name = 'conference_chair'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:track_id>/show_report', views.show_report, name='show_report'),
    path('<int:track_id>/reject_permission', views.reject_permission, name='reject_permission'),
    path('<int:track_id>/give_permission', views.give_permission, name='give_permission'),
]