from django.db import models
from authentication.models import CustomUser
# Create your models here.
class Track(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviewer')
    track_chair = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='track_chair')
    description = models.TextField(blank = True, null = True)