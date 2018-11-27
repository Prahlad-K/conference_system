from django.db import models
 # Create your models here.
class draft(models.Model):
    title=models.CharField(max_length=500)
    text=models.CharField(max_length=500,null=True)