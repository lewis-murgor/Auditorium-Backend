from django.urls import path
from .views import ShowListCreateView, ShowDetailView

urlpatterns = [
    path('', ShowListCreateView.as_view(), name='show-list-create'),
    path('<int:pk>/', ShowDetailView.as_view(), name='show-detail'),
]
