from django.db import models

# Create your models here.

class Performance(models.Model):
    VERYGOOD = 1
    GOOD =2
    AVERAGE = 3
    BELOWAVG = 4
    BAD = 5

    PERF_CHOICES = (
    (VERYGOOD, 'Very good'),
    (GOOD, 'Good'),
    (AVERAGE, 'Average'),
    (BELOWAVG, 'Below Average'),
    (BAD, 'Bad'),
    )
    id = models.PositiveSmallIntegerField(choices=PERF_CHOICES, primary_key=True)

    def __str__(self):
      return self.get_id_display()

class ReviewReport(models.Model):
    problem_statement = models.OneToOneField(Performance, related_name = "ps_perf", on_delete = models.CASCADE, null = True)
    research_sig = models.OneToOneField(Performance, related_name = "rs_perf", on_delete = models.CASCADE, null = True)
    lit_review = models.OneToOneField(Performance, related_name = "lr_perf", on_delete = models.CASCADE, null = True)
    methodology = models.OneToOneField(Performance, related_name = "m_perf", on_delete = models.CASCADE, null = True)

    description = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.description