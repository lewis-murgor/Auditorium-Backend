from django.db import models

# Create your models here.
from django.db import models

class Show(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    time = models.TimeField()
    balcony_seats = models.PositiveIntegerField()
    ordinary_seats = models.PositiveIntegerField()
    price_balcony = models.DecimalField(max_digits=8, decimal_places=2)
    price_ordinary = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} on {self.date} at {self.time}"

