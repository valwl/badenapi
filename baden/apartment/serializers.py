from rest_framework import serializers
from . models import Apartment, ApartmentImg, Category, Location


class ApartmentImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImg
        fields = '__all__'


class ApartmentSerializer(serializers.ModelSerializer):
    images = ApartmentImgSerializer(many=True, required=False)
    class Meta:
        model = Apartment
        fields = '__all__'

    def create(self, validation_data):
        images_data = self.context.get('request').FILES.getlist('images')
        apartment = Apartment.objects.create(
             title=validation_data.get('title'),
             description=validation_data.get('description'),
             location=validation_data.get('location'),
             guest=validation_data.get('guest'),
             category=validation_data.get('category'),
             base_price=validation_data.get('base_price'),
             weekend_price=validation_data.get('weekend_price'),
             is_active=validation_data.get('is_active'),
         )
        for img in images_data:
            ApartmentImg.objects.create(
                img=img,
                apartment=apartment
            )
        return apartment




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'