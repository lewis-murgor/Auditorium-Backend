from django.urls import path
from .views import SalespersonCreateView

urlpatterns = [
    path('create-salesperson/', SalespersonCreateView.as_view(), name='create-salesperson'),
]
