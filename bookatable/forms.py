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
            ("1", "10:00 - 10:45"),
            ("2", "11:00 - 11:45"),
            ("3", "12:00 - 12:45"),
            ("4", "13:00 - 13:45"),
            ("5", "14:00 - 14:45"),
            ("6", "15:00 - 15:45"),
            ("7", "16:00 - 16:45"),
            ("8", "17:00 - 17:45"),
            ("9", "18:00 - 18:45"),
            ("10", "19:00 - 19:45"),
            ("11", "20:00 - 20:45"),
            ("12", "21:00 - 21:45"),
            ("13", "22:00 - 22:45"),
            ],
        help_text="Please select a booking time between 10:00 and 22:45"
    )