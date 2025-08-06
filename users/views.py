from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer
from .permissions import IsShowManagerOnly

# Create your views here.
class SalespersonCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsShowManagerOnly]

    def perform_create(self, serializer):
        serializer.save(role='salesperson')

