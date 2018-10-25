from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
CATEGORIES = (  
    ('LAB', 'labor'),
    ('CAR', 'cars'),
    ('TRU', 'trucks'),
    ('WRI', 'writing'),
)
LOCATIONS = (  
    ('BRO', 'Bronx'),
    ('BRK', 'Brooklyn'),
    ('QNS', 'Queens'),
    ('MAN', 'Manhattan'),
    ('STN', 'Staten Island'),
)

class PostAd(models.Model):  
    name        = models.CharField(max_length=50)
    email       = models.EmailField()
    gist        = models.CharField(max_length=50)
    category    = models.CharField(max_length=3, choices=CATEGORIES)
    location    = models.CharField(max_length=3, choices=LOCATIONS)
    description = models.TextField(max_length=300)
    expire      = models.DateField()
    