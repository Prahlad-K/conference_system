from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

class collectPaymentForm(forms.Form):
    credit_card_no = forms.CharField(help_text = "Enter your credit card no.",max_length=20)
    amount = forms.IntegerField()
    cvv = forms.IntegerField()
    expiry_date = forms.DateField()

    def clean_expiry_date(self):
        data = self.cleaned_data['expiry_date']

        if data < timezone.now().date():
            raise ValidationError(_('Card expired!'))

        return data

class ContactForm(forms.Form):
    email_id = forms.CharField(help_text = "abc@xyz.com",required=True)
    #contact_number = forms.IntegerField()
    subject = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea, required=True)
