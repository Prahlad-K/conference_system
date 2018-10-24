from django.db import models
from authentication.models import CustomUser
# Create your models here.
import datetime 
class Payment(models.Model):
    credit_card_no = models.CharField(max_length=20)
    cvv = models.IntegerField(default = 0)
    expiry_date = models.DateField('expiration date', default = datetime.datetime.today())
    amount = models.IntegerField(default = 200)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null = True)
    payment_date = models.DateTimeField('Date paid')
    started = models.BooleanField(default = False)
    ongoing = models.BooleanField(default = False)
    approved = models.BooleanField(default = False)
    completed = models.BooleanField(default = False)

    def __str__(self):
     return self.credit_card_no
