from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class collectPaymentForm(forms.Form):
    credit_card_no = forms.CharField(help_text = "Enter your credit card no.",max_length=20)
    amount = forms.IntegerField()
    paymentDetails = forms.CharField(max_length=200)
    payment_date = forms.DateTimeField()
    
    def clean_credit_card_no(self):
        data = self.cleaned_data['credit_card_no']

       # if len(data) < 16:
           # raise ValidationError(_('Invalid credit card number'))

        return data

    
    def clean_amount(self):
        data = self.cleaned_data['amount']

      #  if len(data) < 16:
         #   raise ValidationError(_('Invalid amount'))

        return data
    
    def clean_paymentDetails(self):
        data = self.cleaned_data['paymentDetails']

       # if len(data) < 16:
           ## raise ValidationError(_('Invalid payment details'))

        return data
    
    def clean_payment_date(self):
        data = self.cleaned_data['payment_date']

       # if len(data) < 16:
         #   raise ValidationError(_('Invalid payment date'))

        return data
    
        
    