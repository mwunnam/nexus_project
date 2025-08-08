from django.shortcuts import render
from rest_framework import generics, permissions
from customer.models import Customer
from .serializers import CustomerSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
