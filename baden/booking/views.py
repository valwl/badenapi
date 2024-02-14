from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from . serializer import BookingSerializer, ReviewSerializer
import stripe
from . models import Booking, Review
from django.conf import settings
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()


stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class BookingView(APIView):
    def post(self, request, *args, **kwargs,):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            apartment = serializer.validated_data.get('apartment')
            check_in_day = serializer.validated_data.get('check_in_day')
            check_out_day = serializer.validated_data.get('check_out_day')
            bookings = Booking.objects.filter(Q(apartment=apartment) and Q(check_in_day__lte=check_out_day) and Q(check_out_day__gte=check_in_day))
            if not bookings:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        bookings = Booking.objects.filter(user=User)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PaymentView(APIView):
    def post(self, request, *args, **kwargs):
        booking_id = request.data.get('booking_id')
        try:
            booking = Booking.objects.get(pk=booking_id, status='pending')
            token = request.data.get('token')
            total_price = booking.total_price

            charge = stripe.Charge.create(
                total_price=total_price,
                currency='usd',
                description='booking payment',
                source=token,
            )

            booking.status = 'paid'
            booking.save()

            return Response({'message': 'payment success'}, status=status.HTTP_200_OK)
        except Booking.DoesNotExist:
            return Response({'error': 'booking not found or status not pending'},
                            status=status.HTTP_400_BAD_REQUEST)


class ReviewView(viewsets.ModelViewSet):
    model = Review
    serializer = ReviewSerializer



