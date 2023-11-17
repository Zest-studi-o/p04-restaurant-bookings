# Generated by Django 4.2.7 on 2023-11-17 23:54

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('image_url', cloudinary.models.CloudinaryField(blank=True, default='none', max_length=255, null=True, verbose_name='image')),
            ],
        ),
    ]
