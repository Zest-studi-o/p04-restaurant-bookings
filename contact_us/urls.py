"""
Contact App - URLS
----------------
URLS Configuration for Contact App
"""
from django.urls import path
from .views import Contact


urlpatterns = [
    path('', Contact.as_view(), name="contact_us"),
]