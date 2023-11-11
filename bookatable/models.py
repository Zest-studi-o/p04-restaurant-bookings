from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    date = models.DateField()
    booking_time = models.CharField(
        max_length=5,
        choices=[
            ("10:00", "10:00 AM"),
            ("11:00", "11:00 AM"),
            ("12:00", "12:00 PM"),
            ("13:00", "01:00 PM"),
            ("14:00", "02:00 PM"),
            ("15:00", "03:00 PM"),
            ("16:00", "04:00 PM"),
            ("17:00", "05:00 PM"),
            ("18:00", "06:00 PM"),
            ("19:00", "07:00 PM"),
            ("20:00", "08:00 PM"),
            ("21:00", "09:00 PM"),
            ("22:00", "10:00 PM"),
        ],
        default="10:00"  # Set the default value to "10:00"
    )
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    total_tables = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def is_table_available(self):
        """ 
        Calculate the total tables booked 
        for the selected date and time 
        """
    
        booked_tables = Booking.objects.filter(date=self.date, booking_time=self.booking_time).aggregate(Sum('total_tables'))['total_tables__sum'] or 0

        # If the current booking is being updated, subtract its total_tables
        if self.booking_id:
            booked_tables -= self.total_tables
        return booked_tables < 25

    def save(self, *args, **kwargs):
        """ 
        Check table availability 
        """
        if not self.booking_id:
            if not self.is_table_available():
                raise Exception("No tables available for this date and time")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking ID: {self.booking_id}, Date: {self.date}, Time: {self.booking_time}"