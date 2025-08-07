from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Seat, Booking
from .serializers import SeatSerializer, BookingSerializer
from .permissions import IsSpectator, IsBookingOwner, IsSalespersonOrManager
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from datetime import timedelta

from booking import serializers

# Create your views here.
class SeatListCreateView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.IsAuthenticated, IsSalespersonOrManager]


class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsSpectator]

    def perform_create(self, serializer):
        seat = serializer.validated_data['seat']
        if seat.is_booked:
            raise serializers.ValidationError("Seat already booked.")
        seat.is_booked = True
        seat.save()
        serializer.save(spectator=self.request.user)


class BookingCancelView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated, IsSpectator, IsBookingOwner]

    def update(self, request, *args, **kwargs):
        booking = self.get_object()

        if booking.is_cancelled:
            return Response({"detail": "Already cancelled."}, status=status.HTTP_400_BAD_REQUEST)

        booking.is_cancelled = True
        booking.cancelled_at = now()
        booking.refund_amount = booking.calculate_refund()
        booking.save()

        booking.seat.is_booked = False
        booking.seat.save()

        return Response({
            "detail": "Booking cancelled successfully.",
            "refund": booking.refund_amount
        }, status=status.HTTP_200_OK)

