from django.urls import path

from . import views

app_name = 'payment'
urlpatterns = [

    path('', views.index, name='index'),

    path('<int:payment_id>/', views.detail, name='detail'),

    path('<int:payment_id>/start/', views.start, name='start'),

    path('<int:payment_id>/status/', views.status, name='status'),
]