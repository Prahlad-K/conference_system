from django.urls import path
from . import views
app_name = 'authentication'

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('choose_profile', views.choose_profile, name='choose_profile'),
    path('logout', views.logout_view, name='logout_view'),
    path('sign_up', views.sign_up, name='sign_up'),
]