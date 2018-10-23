from django.urls import path
from . import views

app_name = 'registration_manager'

urlpatterns = [

    path('', views.display, name='display'),
    path('payment/', views.index, name='index'),
    path('payment/<int:payment_id>/status', views.status, name='status'),
    path('payment/<int:payment_id>/wait', views.wait, name='wait'),
    path('payment/<int:payment_id>/approve', views.approve, name='approve'),
    path('payment/<int:payment_id>/complete', views.complete, name='complete'),
]