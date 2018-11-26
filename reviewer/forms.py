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

    problem_statement = forms.ChoiceField(choices=PERF_CHOICES, required=True)
    research_sig = forms.ChoiceField(choices=PERF_CHOICES, required=True)
    lit_review = forms.ChoiceField(choices=PERF_CHOICES, required=True)
    methodology = forms.ChoiceField(choices=PERF_CHOICES, required=True)
    description = forms.CharField(max_length=200)
    
    class Meta:
        model = ReviewReport
        fields = ['problem_statement', 'research_sig', 'lit_review', 'methodology', 'description']