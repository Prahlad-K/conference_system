# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Role

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

class CustomUserCreationForm(UserCreationForm):
    roles = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=ROLES_CHOICES,
    )
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password')

class CustomUserChangeForm(UserChangeForm):
    roles = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=ROLES_CHOICES,
    )
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')