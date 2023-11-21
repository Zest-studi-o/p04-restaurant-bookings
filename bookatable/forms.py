from django import forms
from .models import Booking
from django.utils import timezone
from datetime import datetime
from django.db.models import Sum


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date', 'time', "people"]
        labels = {
            "name": "Name",
            "email": "Email",
            "date": "Date",
            "time": "Time",
            "people": "Guests",
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")
        self.validate_future_booking(date)
        self.validate_present_booking(time, date)

    def validate_present_booking(self, time, date):
        if date == timezone.now().date() and time:
            current_time = datetime.now().time().strftime("%H:%M")
            if time < current_time:
                raise forms.ValidationError("Please select a future time")

    def validate_future_booking(self, date):
        if date and date < timezone.now().date():
            raise forms.ValidationError("Please select a future date")

    date = forms.DateField(
        help_text="Please select a date",
        widget=forms.widgets.DateInput(attrs={"type": "date"}),
    )
    time = forms.ChoiceField(
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

