from django.shortcuts import render
from .models import *
from .serializers import *
from django.utils.timezone import localtime
import pytz
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

# List of all upcoming fitness classes
@api_view(['GET'])
def get_classes(request):
    classes = FitnessClass.objects.all()
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)


# Book class 
@api_view(['POST'])
def book_class(request):
    data = request.data 
    required_fields = ['class_id', 'client_name', 'client_email']
    for field in required_fields:
        if field not in data:
            return Response({'error': f'{field} is required.'}, status=400)
        
    try:
        fitness_class = FitnessClass.objects.get(id=data['class_id'])
    except FitnessClass.DoesNotExist:
        return Response({'error': 'Class not found'}, status=404)
    
    if fitness_class.available_slots <= 0 :
        return Response({'error': 'No slots available'}, status=400)
    
    # Create booking
    booking = Booking.objects.create(
        fitness_class=fitness_class,
        client_name=data['client_name'],
        client_email=data['client_email']
    )

    # Update available slots
    fitness_class.available_slots -= 1
    fitness_class.save()

    serializer = BookingSerializer(booking)
    return Response(serializer.data, status=201)



#  All bookings made by a specific email address
@api_view(['GET'])
def get_bookings(request):
    email = request.GET.get('email')
    
    if not email:
        return Response({'error': 'Email parameter is required'}, status=400)

    bookings = Booking.objects.filter(client_email=email)
    
    if not bookings.exists():
        return Response({'error': 'No bookings found for this email'}, status=404)

    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

