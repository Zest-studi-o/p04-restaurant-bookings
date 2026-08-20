import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creates or updates a superuser using environment variables for username, email, and password.'

    def handle(self, *args, **options):
        User = get_user_model()
        
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not password:
            self.stdout.write(self.style.ERROR('No password provided in environment variables.'))
            return

        if not username:
            self.stdout.write(self.style.ERROR('No username provided in environment variables.'))
            return

        user, created = User.objects.get_or_create(username=username, defaults={'email': email or ''})
        
        # Ensure the user has staff and superuser permissions and update credentials
        user.set_password(password)
        if email:
            user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" updated successfully with new credentials.'))