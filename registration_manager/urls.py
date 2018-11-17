from django.urls import path
from . import views

app_name = 'registration_manager'

urlpatterns = [

    path('', views.display, name='display'),
    path('<int:payment_id>/approve', views.approve, name='approve'),
    path('<int:payment_id>/delete', views.delete, name = 'delete'),
    path('<int:user_id>/approve_user',views.approve_user,name='approve_user')
]