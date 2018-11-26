from django.db import models
from authentication.models import CustomUser

from author.models import ResearchPaper
from reviewer.models import ReviewReport
from authentication.models import CustomUser


# Create your models here.
class Track(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviewer')
    track_chair = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='track_chair')
    description = models.TextField(blank = True, null = True)
    paper = models.ForeignKey(ResearchPaper,on_delete=models.CASCADE,related_name='respaper',null=True)
    report = models.ForeignKey(ReviewReport,on_delete=models.CASCADE,related_name='respaper',null=True)
    paper_submitted = models.BooleanField(default = False)
    report_submitted = models.BooleanField(default = False)
    permission_requested = models.BooleanField(default = False)
    track_approved = models.BooleanField(default = False)

class ConferenceTypes(models.Model):
    WORKSHOP = 1
    SEMINAR = 2
    CONFERENCE = 3

    CONFERENCE_CHOICES = (
      (WORKSHOP, 'Workshop'),
      (SEMINAR, 'Seminar'),
      (CONFERENCE, 'Conference')
    ) 

    id = models.PositiveSmallIntegerField(choices=CONFERENCE_CHOICES, primary_key=True)

    def __str__(self):
      return self.get_id_display()
    
class Conference(models.Model):
    conference_name = models.TextField(blank = True, null = True)
    conference_date = models.DateField()
    conference_type = models.ForeignKey(ConferenceTypes, on_delete = models.CASCADE)
    registration_manager = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='registration_manager', null = True)
    conference_chair = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='conference_chair')
    conference_manager = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='conference_manager')
