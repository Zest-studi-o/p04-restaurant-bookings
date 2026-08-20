from django.shortcuts import render
"""
Contact App - Views
"""
from django.views.generic import TemplateView


class Contact(TemplateView):
    """
    A view to load the contact html template
    """
    template_name = "contact.html"