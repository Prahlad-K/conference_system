import django
from authentication.models import CustomUser, Role
from django.contrib.auth.models import Group

def run():
    # Create super user
    u = CustomUser.objects.create_superuser(username = 'superuser1', email='123@gmail.com', password = 'Group@123')

    print("\nSuperuser with the following details created - \nusername : superuser1 \npassword : Group@123\n")

    u.roles.add(Role.objects.create(id=1))
    u.roles.add(Role.objects.create(id=2))
    u.roles.add(Role.objects.create(id=3))
    u.roles.add(Role.objects.create(id=4))
    u.roles.add(Role.objects.create(id=5))
    u.roles.add(Role.objects.create(id=6))

    print("All the roles have been assigned to the superuser. You may now run the server and log in.\n")


