"""
Menu App - Admin
----------------
Admin Configuration for Menu App.
"""
from django.contrib import admin

from .models import MenuItem


# Register your models here.
@admin.register(MenuItem)
class Menu(admin.ModelAdmin):
    list_display = (
        "menu_name",
        "description",
        "image_url",
        "price",
        "category"
    )
