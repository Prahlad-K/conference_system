from django import forms 
from .models import ResearchPaper

ABSTRACT = 1
FULL_PROPOSAL = 2 
BOTH = 3
SUBMISSION_CHOICES = (
    (ABSTRACT,'Abstract'),
    (FULL_PROPOSAL,'Full Proposal'),
    (BOTH,'Both'),
)

class AdPaperForm(forms.ModelForm):  
    error_css_class = 'error'
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Research Paper Title'}))
    authors = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Authors for this Paper'}))

    type = forms.ChoiceField(choices=SUBMISSION_CHOICES, required=True,widget=forms.Select(attrs={'class':'form-control'}))
    docfile = forms.FileField(
                label='Select a file',
                help_text='max. 42 megabytes'
              )
    class Meta:
        model = ResearchPaper
        fields = ['title', 'authors', 'type', 'docfile']
        