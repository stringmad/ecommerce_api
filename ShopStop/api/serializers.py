from rest_framework.serializers import ModelSerializer, CharField
from django.db import models
from .models import Product,Category,Vendor,SubCategory
from rest_framework import serializers

class DetailSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source=Category.name, read_only=True)
    #mage_by_user = serializers.PrimaryKeyRelatedField( many=True, queryset=Category.objects.all())
    
    class Meta:
        model = Product
        #fields =   [ 'Catagories']
        #fields = [ 'name','price','description']
        fields =  '__all__'
class CategorySerializer(serializers.ModelSerializer):
    Catagories = DetailSerializer(many=True, read_only=True)
    #Catagories = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields =  '__all__'
    ##def get_Catagories(self, obj):
       # qs = obj.Catagories.all()
       # return DetailSerializer(qs, many=True).data

class CategorydetSerializer(serializers.ModelSerializer):

       class Meta:
        model = Category
        fields =  '__all__'
class VendordetSerializer(serializers.ModelSerializer):

       class Meta:
        model = Vendor
        fields =  '__all__'

class SubCategorySerializer(serializers.ModelSerializer):

       class Meta:
        model = SubCategory
        fields =  '__all__'