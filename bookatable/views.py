from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.db.models import Sum
from django.core.exceptions import ValidationError


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookatable'
    ordering = ['-created_on']

    def get_queryset(self):
        return Booking.objects.filter(created_by=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    template_name = 'booking_form.html'
    form_class = BookingForm
    success_url = reverse_lazy('booking-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user

        # Check availability for the selected date and time
        selected_date = form.cleaned_data['date']
        selected_time = form.cleaned_data['booking_time']

        total_tables_on_datetime = Booking.objects.filter(date=selected_date, booking_time=selected_time).aggregate(Sum('total_tables'))['total_tables__sum'] or 0

        if total_tables_on_datetime + form.instance.total_tables <= 25:
            form.save()
            messages.success(self.request, 'Booking successful!')
        else:
            messages.error(self.request, 'Sorry, table not available for your selection')
        try:
            return super().form_valid(form)
        except ValidationError:
            return HttpResponseRedirect(self.request.path)


class BookingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Booking
    template_name = 'booking_form.html'
    form_class = BookingForm
    success_url = reverse_lazy('booking-list')

    def test_func(self):
        return self.request.user == self.get_object().created_by

    def form_valid(self, form):
        messages.success(self.request, 'Booking has been updated successfully!')
        return super().form_valid(form)


class BookingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Booking has been deleted successfully')
        return super().delete(request, *args, **kwargs)

    success_url = reverse_lazy('booking-list')

    def test_func(self):
        return self.request.user == self.get_object().created_by