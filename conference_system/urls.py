"""conference_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls', namespace="authentication")),
    path('author/', include('author.urls', namespace="author")),
    path('reviewer/', include('reviewer.urls', namespace="reviewer")),
    path('track_chair/', include('track_chair.urls', namespace="track_chair")),
    path('conference_chair/', include('conference_chair.urls', namespace="conference_chair")),
    path('registration_manager/', include('registration_manager.urls', namespace="registration_manager")),
    path('conference_manager/', include('conference_manager.urls', namespace="conference_manager")),
    path('payment_app/', include('payment_app.urls', namespace="payment_app")),
    path('email_system/',include('email_system.urls',namespace="email_system")),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
