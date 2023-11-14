from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "customer_email",
        "date",
        "booking_time",
        "total_tables",
        "people",
        )