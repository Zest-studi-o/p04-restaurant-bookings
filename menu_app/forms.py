from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["menu_name", "description", "category", "price", "image_url"]
        labels = {
            "menu_name": "Dish Name",
            "description": "Description",
            "image_url": "Image",
            "price": "Price",
            "category": "Category",
        }