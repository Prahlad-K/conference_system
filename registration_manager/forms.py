from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class collectPaymentForm(forms.Form):
    credit_card_no = forms.CharField(help_text = "Enter your credit card no.",max_length=20)
    amount = forms.IntegerField()
    
        
    