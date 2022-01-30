from django.shortcuts import render
from .models import Product,Category
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, serializers, status
from .serializers import DetailSerializer,CategorySerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.views import exception_handler


# Create your views here.

class FilterOrderView(generics.ListAPIView):
     #permission_classes = (AllowAny,)
     queryset = Product.objects.all()
     serializer_class = DetailSerializer
     filter_backends = [filters.DjangoFilterBackend,SearchFilter, OrderingFilter]
     search_fields = [ 'name','price','category__name','subcategory__name','Vendor_name__name']
     ordering_fields = ['price', 'Vendor_name__name','category__name','subcategory__name']
     filter_fields = {
        'price': ['gte', 'lte'],
        'category__name':['exact'],
        'subcategory__name':['exact'],
    }
class ListallView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


