from django.shortcuts import render
from rest_framework import generics
from .models import Products
from .serializer import ProductSerializer

# Create your views here.
class ProductDetailView(generics.RetrieveAPIView): # RetrieveAPIView --> basically works as get method and retrieves the data of one single method
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer