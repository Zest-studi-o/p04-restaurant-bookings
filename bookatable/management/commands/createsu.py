import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creates a superuser using environment variables for username, email, and password.'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Leemos los datos de las variables de entorno de Render
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not password:
            self.stdout.write(self.style.ERROR('No password provided in environment variables.'))
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))
        else:
            self.stdout.write(self.style.WARNING(f'The superuser "{username}" already exists.'))