from django.shortcuts import render
from .models import Order, OrderItem
from rest_framework import generics, permissions
from .serializers import OrderSerialiazer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerialiazer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
