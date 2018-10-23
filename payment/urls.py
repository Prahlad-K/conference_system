from django.urls import path

from . import views

app_name = 'payment'
urlpatterns = [

    path('', views.index, name='index'),
    path('<int:payment_id>/status', views.status, name='status'),
    path('<int:payment_id>/approve', views.approve, name='approve'),
]