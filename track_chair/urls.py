from django.urls import path
from . import views

app_name = 'track_chair'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:track_id>/approve', views.approve, name='approve'),
    path('<int:track_id>/show_report', views.show_report, name='show_report'),
    path('<int:track_id>/revert_permission', views.revert_permission, name='revert_permission'),
    path('<int:track_id>/redo_report', views.redo_report, name='redo_report'),
]