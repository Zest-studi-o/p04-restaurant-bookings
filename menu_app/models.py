from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings


class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = CloudinaryField(
        "image",
        default="none",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name