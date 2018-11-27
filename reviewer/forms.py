from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .models import ReviewReport

PERF_CHOICES = (
('VERYGOOD', 'Very good'),
('GOOD', 'Good'),
('AVERAGE', 'Average'),
('BELOWAVG', 'Below Average'),
('BAD', 'Bad'),
)


class ReviewForm(forms.ModelForm):  
    error_css_class = 'error'

    problem_statement = forms.ChoiceField(choices=PERF_CHOICES, required=True,widget=forms.Select(attrs={'class':'form-control'}))
    research_sig = forms.ChoiceField(choices=PERF_CHOICES, required=True,widget=forms.Select(attrs={'class':'form-control'}))
    lit_review = forms.ChoiceField(choices=PERF_CHOICES, required=True,widget=forms.Select(attrs={'class':'form-control'}))
    methodology = forms.ChoiceField(choices=PERF_CHOICES, required=True,widget=forms.Select(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = ReviewReport
        fields = ['problem_statement', 'research_sig', 'lit_review', 'methodology', 'description']