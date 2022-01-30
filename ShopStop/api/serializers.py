from rest_framework.serializers import ModelSerializer, CharField
from django.db import models
from .models import Product,Category
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

