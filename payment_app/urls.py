from django.urls import path
from . import views

app_name = 'payment_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:payment_id>/status', views.status, name='status'),
    path('<int:payment_id>/wait', views.wait, name='wait'),
    path('<int:payment_id>/complete', views.complete, name='complete'),
]