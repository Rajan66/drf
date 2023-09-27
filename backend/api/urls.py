from django.urls import path
from .views import api_home,api_products

urlpatterns = [
    path('',api_home,name="home"),
    path('products/',api_products,name="products"),
]
