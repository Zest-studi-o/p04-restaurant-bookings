from django.views.generic import ListView
from django.shortcuts import render
from .models import MenuItem


class MenuListView(ListView):
    """View menu list"""
    model = MenuItem
    template_name = "menu_list.html"