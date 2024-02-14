from django.urls import path
from . views import BookingView, PaymentView


urlpatterns = [
    path('booking/', BookingView.as_view()),
    path('payment/', PaymentView.as_view()),
]