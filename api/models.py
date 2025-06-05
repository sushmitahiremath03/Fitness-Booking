from django.db import models
from django.utils import timezone


# Create your models here.
class FitnessClass(models.Model):
    CLASS_TYPES = [
        ('Yoga', 'Yoga'),
        ('Zumba', 'Zumba'),
        ('HIIT', 'HIIT'),
    ]

    name = models.CharField(max_length=100,choices=CLASS_TYPES)
    instructor = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    total_slots = models.IntegerField()
    available_slots = models.IntegerField()

    def __str__(self):
        return f"{self.name} with {self.instructor} at {self.datetime}"
    

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} ({self.client_email}) booked {self.fitness_class}"

