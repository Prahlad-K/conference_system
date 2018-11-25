from django import forms
from .models import draft

class DraftForm(forms.ModelForm):

    class Meta:
        model=draft
        fields=('title','text',)
    
