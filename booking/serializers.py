from rest_framework import serializers
from .models import Seat, Booking

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    seat_number = serializers.CharField(source='seat.seat_number', read_only=True)
    seat_type = serializers.CharField(source='seat.seat_type', read_only=True)
    show_date = serializers.DateField(source='seat.show.date', read_only=True)
    show_time = serializers.TimeField(source='seat.show.time', read_only=True)
    price = serializers.DecimalField(source='seat.price', max_digits=8, decimal_places=2, read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'seat', 'seat_number', 'seat_type', 'show_date', 'show_time', 'price', 'is_cancelled', 'refund_amount']
    read_only_fields = ['seat_number', 'seat_type', 'show_date', 'show_time', 'price']