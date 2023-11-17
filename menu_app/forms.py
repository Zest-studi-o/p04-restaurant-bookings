from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["name", "description", "price", "image_url"]
        labels = {
            "name": "Dish Name",
            "description": "Description",
            "image_url": "Image",
            "price": "Price",
        }