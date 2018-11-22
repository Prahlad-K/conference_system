from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Role(models.Model):
  AUTHOR = 1
  REVIEWER = 2
  TRACKCHAIR = 3
  CONFERENCECHAIR = 4
  REGISTRATIONMANAGER = 5
  CONFERENCEMANAGER = 6
  ROLES_CHOICES = (
      (AUTHOR, 'Author'),
      (REVIEWER, 'Reviewer'),
      (TRACKCHAIR, 'Track Chair'),
      (CONFERENCECHAIR, 'Conference Chair'),
      (REGISTRATIONMANAGER, 'Registration Manager'),
      (CONFERENCEMANAGER, 'Conference Manager'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLES_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()


class CustomUser(AbstractUser):
  roles = models.ManyToManyField(Role)
  validated = models.BooleanField(default=False)

  def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)