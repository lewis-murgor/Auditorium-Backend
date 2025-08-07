from django.urls import path
from .views import SeatListCreateView, BookingCreateView, BookingCancelView

urlpatterns = [
    path('seats/', SeatListCreateView.as_view(), name='seat-list-create'),
    path('bookings/', BookingCreateView.as_view(), name='booking-create'),
    path('bookings/<int:pk>/cancel/', BookingCancelView.as_view(), name='booking-cancel'),
]
