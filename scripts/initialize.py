import django
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

def run():
    # Create super user
    User.objects.create_superuser('superuser1', 'admin@portal.com', 'Group@123')

    print("Superuser created...")

    # Create groups
    Group.objects.create(name='Author')
    Group.objects.create(name='Reviewer')
    Group.objects.create(name='Track Chair')
    Group.objects.create(name='Conference Chair')
    Group.objects.create(name='Registration Manager')

    print("Groups created...")