from django.db import models

# Create your models here.

class Payment(models.Model):
    paymentDetails = models.CharField(max_length=200)
    payment_date = models.DateTimeField('Date paid')
    started = models.BooleanField(default = False)
    ongoing = models.BooleanField(default = False)
    approved = models.BooleanField(default = False)
    completed = models.BooleanField(default = False)

    def __str__(self):
     return self.paymentDetails
