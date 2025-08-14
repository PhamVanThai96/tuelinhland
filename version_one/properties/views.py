from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Property, PropertyType
from .serializers import PropertyListSerializer, PropertyDetailSerializer, PropertyTypeSerializer


class PropertyTypeListView(generics.ListAPIView):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer


class PropertyListView(generics.ListAPIView):
    queryset = Property.objects.filter(status='available')
    serializer_class = PropertyListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['property_type', 'district', 'city', 'bedrooms', 'featured']
    search_fields = ['title', 'description', 'address']
    ordering_fields = ['price', 'area', 'created_at']
    ordering = ['-created_at']


class PropertyDetailView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer


class FeaturedPropertyListView(generics.ListAPIView):
    queryset = Property.objects.filter(featured=True, status='available')
    serializer_class = PropertyListSerializer
    ordering = ['-created_at']
