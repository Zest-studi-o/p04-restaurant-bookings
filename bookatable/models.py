from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


PEOPLE = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "4"), (6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10"), (11, "11"), (12, "12"))

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True) # Set this to primary key
    date = models.DateField()
    booking_time = models.CharField(
        max_length=20,
        choices=[ 
            ("10:00", "10:00 - 10:45"),
            ("11:00", "11:00 - 11:45"),
            ("12:00", "12:00 - 12:45"),
            ("13:00", "13:00 - 13:45"),
            ("14:00", "14:00 - 14:45"),
            ("15:00", "15:00 - 15:45"),
            ("16:00", "16:00 - 16:45"),
            ("17:00", "17:00 - 17:45"),
            ("18:00", "18:00 - 18:45"),
            ("19:00", "19:00 - 19:45"),
            ("20:00", "20:00 - 20:45"),
            ("21:00", "21:00 - 21:45"),
            ("22:00", "22:00 - 22:45"),
        ],
         default="10:00 - 10:45"  #Set the default value to "10:00- 10:45"
    )
    customer_name = models.CharField(max_length=255) # Name 
    customer_email = models.EmailField() # Email
    people = models.IntegerField(choices=PEOPLE, default=2) # To select how many people 
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE) # Set this to foreign key

    def is_table_available(self):
        """ 
        Calculate the total tables booked 
        for the selected date and time slot
        """
    
        booked_tables = Booking.objects.filter(date=self.date, booking_time=self.booking_time).aggregate(Sum('people'))['people__sum'] or 0

        # If the current booking is being updated, subtract its people
        if self.booking_id:
            booked_tables -= self.people
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