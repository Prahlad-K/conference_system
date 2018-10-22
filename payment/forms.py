from django import forms
from django.core.exceptions import ValidationError

class collectPaymentForm(forms.Form):
    credit_card_no = forms.CharField(help_text = "Enter your credit card no.",max_length=20)

    def clean_credit_card_no(self):
        data = self.cleaned_data['credit_card_no']

        return data
        