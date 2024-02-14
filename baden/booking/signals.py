from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from . models import Payment, Booking
from datetime import datetime


@receiver(pre_save, sender=Booking)
def update_booking_status(sender, instance, **kwargs):
    if instance.status == 'paid' and instance.check_out_day <= datetime.now():
        instance.status = 'complete'
        instance.save()
