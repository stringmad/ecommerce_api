from django.conf import settings
from django.conf.urls.static import static
from .views import FilterOrderView,ListallView
from django.urls import path, include

urlpatterns = [
    path(r'productview/',FilterOrderView.as_view()),
    path(r'productlist/',ListallView.as_view()),
   ]
   