# Generated by Django 4.2.7 on 2023-11-16 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookatable', '0005_remove_booking_total_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='people',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '4'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12')], default=2),
        ),
    ]