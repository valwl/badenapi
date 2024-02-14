from django.shortcuts import render
from . serializers import ApartmentSerializer, ApartmentImgSerializer, LocationSerializer, CategorySerializer
from rest_framework import viewsets
from . models import Apartment, ApartmentImg, Category, Location
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import mixins


class ApartmentView(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer

    @action(methods=['get'], detail=True)
    def get_img(self, request, pk):
        # apartment = Apartment.objects.get(pk=pk)
        apartment_img = ApartmentImg.objects.filter(apartment=pk)
        return Response({'imges': ApartmentImgSerializer(apartment_img, many=True).data})


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LocationView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ApartmentImgViews(generics.ListAPIView):
    queryset = ApartmentImg.objects.all()
    serializer_class = ApartmentImgSerializer

