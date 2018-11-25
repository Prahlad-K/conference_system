from django.apps import AppConfig


class EmailConfig(AppConfig):
    name = 'email_system'
#    label = 'my.email_system'  # <-- this is the important line - change it to anything other than the default, which is the module name ('foo' in this case)
