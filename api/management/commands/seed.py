from django.core.management.base import BaseCommand
from api.models import FitnessClass
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        FitnessClass.objects.all().delete()
        classes = [
            {'name': 'Yoga', 'instructor': 'Amit', 'days_from_now': 1},
            {'name': 'Zumba', 'instructor': 'Priya', 'days_from_now': 2},
            {'name': 'HIIT', 'instructor': 'Raj', 'days_from_now': 3},
        ]
        for cls in classes:
            dt = make_aware(datetime.now() + timedelta(days=cls['days_from_now']))
            FitnessClass.objects.create(name=cls['name'], instructor=cls['instructor'], datetime=dt, total_slots=10, available_slots=10)
        self.stdout.write("Seed data added.")
