from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('manager', 'Show Manager'),
        ('salesperson', 'Salesperson'),
        ('clerk', 'Accounts Clerk'),
        ('spectator', 'Spectator'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)

    def is_manager(self):
        return self.role == 'manager'

    def is_salesperson(self):
        return self.role == 'salesperson'

    def is_clerk(self):
        return self.role == 'clerk'

    def is_spectator(self):
        return self.role == 'spectator'

    def __str__(self):
        return f"{self.username} ({self.role})"
