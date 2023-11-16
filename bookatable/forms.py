from django import forms
from .models import Booking
from django.utils import timezone
from datetime import datetime
from django.db.models import Sum


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'date', 'booking_time', "people"]
        labels = {
            "customer_name": "Customer Name",
            "customer_email": "Customer Email",
            "date": "Date",
            "booking_time": "Booking Time",
            "people": "Guests",
    }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        if date and date < timezone.now().date():
            raise forms.ValidationError("Date must be a future date")

        booking_time = cleaned_data.get("booking_time")
        if date == timezone.now().date() and booking_time:
            current_time = datetime.now().time().strftime("%H:%M")
            if booking_time < current_time:
                raise forms.ValidationError("Booking time can not be in the past")

    date = forms.DateField(
        help_text="Date must be a future date",
        widget=forms.widgets.DateInput(attrs={"type": "date"}),
    )
    booking_time = forms.ChoiceField(
        choices=[
            ("10:00", "10:00 - 10:45"),
            ("11:00", "11:00 - 11:45"),
            ("12:00", "12:00 - 12:45"),
            ("13:00 ", "13:00 - 13:45"),
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
        help_text="Please select a booking time between 10:00 and 22:45"
    )