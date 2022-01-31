from django.shortcuts import render
from .models import Product,Category,Vendor,SubCategory
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics, serializers, status
from .serializers import DetailSerializer,CategorySerializer,CategorydetSerializer,VendordetSerializer,SubCategorySerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.views import exception_handler
from rest_framework.views import APIView
from rest_framework.response import Response
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

class CategoryView(APIView):
    def get(self,request,id=None):
     if id: 
         item = Category.objects.get(id=id)
         serializer = CategorydetSerializer(item)
         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
     queryset = Category.objects.all()
     serializer_class = CategorydetSerializer(queryset,many=True)
     return Response(serializer_class.data)

class VendorView(APIView):
    def get(self,request,id=None):
     if id: 
         item = Vendor.objects.get(id=id)
         serializer = VendordetSerializer(item)
         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
     queryset = Vendor.objects.all()
     serializer_class = VendordetSerializer(queryset,many=True)
     return Response(serializer_class.data)
class SubCategoryView(APIView):
    def get(self,request,id=None):
     if id: 
         item = SubCategory.objects.get(id=id)
         serializer = SubCategorySerializer(item)
         return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
     queryset = SubCategory.objects.all()
     serializer_class = SubCategorySerializer(queryset,many=True)
     return Response(serializer_class.data)