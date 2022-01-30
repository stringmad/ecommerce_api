from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
from django.db.models import (Model, TextField, DateTimeField, ForeignKey,CASCADE)

#This user_directory_path is used to store images in a folder
def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'product/{filename}'.format(filename=filename)
#This choice field is used to differentiate regions

Region_CHOICES = [
    ('EU', 'Europe Region'),
    ('US', 'America Region'),
    ('China', 'China Region'),
    ('ROW', 'Rest of the World'),
]

class PricingRange(models.Model):
 minprice = models.FloatField(max_length=150, db_index=True)
 maxprice = models.FloatField(max_length=150,  db_index=True)
 def __str__(self):
  return 'Between '+str(self.minprice)+' '+str(self.maxprice)

#This model stores vendor details

class Vendor(models.Model):
 name = models.CharField(max_length=150, db_index=True)
 license = models.CharField(max_length=150, db_index=True)
 def __str__(self):
  return self.name

#This model stores Categories

class Category(models.Model):
 name = models.CharField(max_length=150, db_index=True)
 slug = models.SlugField(max_length=150, unique=True, db_index=True)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
 def __str__(self):
  return self.name
 class Meta:
  ordering = ('-created_at', )
  verbose_name = 'category'
  verbose_name_plural = 'categories'

#This model stores SubCategories
class SubCategory(models.Model):
 category = models.ForeignKey(
 Category, related_name='Parent', on_delete=models.CASCADE)
 name = models.CharField(max_length=150, db_index=True)
 slug = models.SlugField(max_length=150, unique=True, db_index=True)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
 def __str__(self):
  return self.name
class Meta:
 ordering = ('-created_at', )
 verbose_name = 'sub-category'
 verbose_name_plural = 'sub-categories'

#This model stores all products

class Product(models.Model):
 name = models.CharField(max_length=100, db_index=True)
 slug = models.SlugField(max_length=100, unique=True, db_index=True)
 price = models.FloatField(max_length=100, db_index=True)
 category = models.ForeignKey(
Category, related_name='Catagories', on_delete=models.CASCADE)
 subcategory = models.ForeignKey(
 SubCategory, related_name='SubCats', on_delete=models.CASCADE)
 description = models.CharField(max_length=350, blank=True, null=True)
 created_at = models.DateTimeField(auto_now_add=True)
 updated_at = models.DateTimeField(auto_now=True)
 price_id = models.ForeignKey(
 PricingRange, related_name='rangebetween', on_delete=models.CASCADE)
 profile_pic = models.ImageField(upload_to =user_directory_path,default='default.jpg',blank=True)
 Vendor_name = models.ForeignKey(
 Vendor, related_name='Vendorlists', on_delete=models.CASCADE)
 region = models.CharField(max_length=100, db_index=True,choices=Region_CHOICES)
 def __str__(self):
  return self.name

class Meta:
 ordering = ["-created_at", "-updated_at"]
