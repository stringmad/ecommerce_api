from django.conf import settings
from django.conf.urls.static import static
from .views import FilterOrderView,ListallView,VendorView,SubCategoryView,CategoryView
from django.urls import path, include

urlpatterns = [
    path(r'productview/',FilterOrderView.as_view()),
    path(r'productlist/',ListallView.as_view()),

    path(r'CategoryView/<int:id>',CategoryView.as_view()),
    path(r'SubCategoryView/<int:id>',SubCategoryView.as_view()),
    path(r'VendorView/<int:id>',VendorView.as_view()),
   
   path(r'CategoryView',CategoryView.as_view()),
    path(r'SubCategoryView',SubCategoryView.as_view()),
    path(r'VendorView',VendorView.as_view()),
   
   
   
   ]
   