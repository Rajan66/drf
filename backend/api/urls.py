from django.urls import path
from .views import api_home,api_products

urlpatterns = [
    path('',api_home,name="home"),
    path('demo/',api_products,name="demo"),
]
