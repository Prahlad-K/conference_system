from django.db import models

# Create your models here.

PERF_CHOICES = (
('VERYGOOD', 'Very good'),
('GOOD', 'Good'),
('AVERAGE', 'Average'),
('BELOWAVG', 'Below Average'),
('BAD', 'Bad'),
)

class ReviewReport(models.Model):
    problem_statement = models.CharField(max_length = 30, choices = PERF_CHOICES, null = True)
    research_sig = models.CharField(max_length = 30, choices = PERF_CHOICES, null = True)
    lit_review = models.CharField(max_length = 30, choices = PERF_CHOICES, null = True)
    methodology = models.CharField(max_length = 30, choices = PERF_CHOICES, null = True)
    
    description = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.description