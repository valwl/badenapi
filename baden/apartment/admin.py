from django.contrib import admin
from . models import Apartment, ApartmentImg, LocationImg, Location,  Category


admin.site.register(Apartment)
admin.site.register(ApartmentImg)
admin.site.register(Location)
admin.site.register(LocationImg)
# admin.site.register(BlocketDate)
admin.site.register(Category)
