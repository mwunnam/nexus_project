from django.shortcuts import render
from rest_framework import generics, permissions
from customer.models import Customer
from order.models import Order
from order.serializers import OrderSerializer
from .serializers import CustomerSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomerOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Order.objects.filter(customer_id=customer_id)
