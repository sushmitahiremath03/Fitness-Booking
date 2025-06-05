from django.test import TestCase
from django.test import TestCase
from .models import FitnessClass
from django.utils import timezone
from datetime import timedelta

# Create your tests here.

# This class defines unit tests for the FitnessClass model
class FitnessClassModelTest(TestCase):
    def test_create_fitness_class(self):
        # Set a future date/time for the class (1 day from now)
        future_time = timezone.now() + timedelta(days=1)
        fc = FitnessClass.objects.create(
            name="Test Class",
            instructor="Test Instructor",
            datetime=future_time,
            total_slots=10,
            available_slots=10
        )
        self.assertEqual(fc.name, "Test Class")
        self.assertEqual(fc.available_slots, 10)