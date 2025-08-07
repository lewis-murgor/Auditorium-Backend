from django.db import models
from django.conf import settings
from shows.models import Show
from datetime import date

# Create your models here.
class Seat(models.Model):
    SEAT_TYPE_CHOICES = [
        ('ordinary', 'Ordinary'),
        ('balcony', 'Balcony'),
    ]

    seat_type = models.CharField(max_length=10, choices=SEAT_TYPE_CHOICES)
    seat_number = models.CharField(max_length=10)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='seats')
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.seat_type.capitalize()} Seat {self.seat_number} for {self.show}"


class Booking(models.Model):
    spectator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    seat = models.OneToOneField(Seat, on_delete=models.PROTECT)
    salesperson = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='sales')
    booked_at = models.DateTimeField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)
    cancelled_at = models.DateTimeField(null=True, blank=True)
    refund_amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def calculate_refund(self):
        if not self.is_cancelled:
            return 0

        show_date = self.seat.show.date
        days_left = (show_date - date.today()).days
        price = self.seat.show.balcony_price if self.seat.seat_type == 'balcony' else self.seat.show.ordinary_price

        if days_left >= 3:
            return price - 5
        elif 1 <= days_left < 3:
            return price - (15 if self.seat.seat_type == 'balcony' else 10)
        elif days_left == 0:
            return price * 0.5
        return 0

    def __str__(self):
        return f"Booking by {self.spectator.username} for {self.seat}"
