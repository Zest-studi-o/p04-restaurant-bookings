from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.db.models import Sum
from django.core.exceptions import ValidationError


class BookingListView(LoginRequiredMixin, ListView):
    """
    Creates views for the list of bookings
    """
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookatable'
    ordering = ['-created_on']

    def get_queryset(self):
        return Booking.objects.filter(created_by=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class BookingCreateView(LoginRequiredMixin, CreateView):
    """
    Creates views for a bookings
    """
    model = Booking
    template_name = 'booking_form.html'
    form_class = BookingForm
    success_url = reverse_lazy('booking-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        # Check availability for the selected date and time
        selected_date = form.cleaned_data['date']
        selected_time = form.cleaned_data['time']

        bookings = Booking.objects.filter(date=selected_date,
                                          time=selected_time)
        people_on_datetime = bookings.aggregate(
            Sum('people'))['people__sum'] or 0
        return super().form_valid(form)
    """
    Success message for a booking
    """

    def get_success_url(self):
        messages.success(self.request, 'Your booking has been successful!')
        return reverse_lazy('booking-list')


class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Enables to update the booking
    """
    model = Booking
    template_name = 'booking_form.html'
    form_class = BookingForm
    success_url = reverse_lazy('booking-list')

    def test_func(self):
        return self.request.user == self.get_object().created_by

    def form_valid(self, form):
        messages.success(self.request,
                         'Your booking has been updated successfully!')
        return super().form_valid(form)


class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Enables to delete the booking
    """
    model = Booking
    template_name = 'booking_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,
                         'Your booking has been deleted successfully')
        return super().delete(request, *args, **kwargs)

    success_url = reverse_lazy('booking-list')

    def test_func(self):
        return self.request.user == self.get_object().created_by