from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime
ABSTRACT = 1
FULL_PROPOSAL = 2 
BOTH = 3
SUBMISSION_CHOICES = (
    (ABSTRACT,'Abstract'),
    (FULL_PROPOSAL,'Full Proposal'),
    (BOTH,'Both'),
)
 
class ResearchPaper(models.Model):
    title = models.CharField(max_length=200,null=True)
    authors = models.CharField(max_length=100,null=True)
    type = models.IntegerField(choices=SUBMISSION_CHOICES)
    docfile = models.FileField(upload_to='research_papers',null=True)
    submission_date = models.DateField(default=datetime.date.today)
    days_left = models.IntegerField(null = True)