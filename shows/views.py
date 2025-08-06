from django.shortcuts import render
from rest_framework import generics
from .models import Show
from .serializers import ShowSerializer
from .permissions import IsManagerOrReadOnly

# Create your views here.
class ShowListCreateView(generics.ListCreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    permission_classes = [IsManagerOrReadOnly]

class ShowDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    permission_classes = [IsManagerOrReadOnly]
