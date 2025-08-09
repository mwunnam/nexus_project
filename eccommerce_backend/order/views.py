from django.shortcuts import render
from .models import Order, OrderItem
from rest_framework import generics, permissions
from .serializers import OrderSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrdersByProductListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        return Order.objects.filter(item).distinct().order_by('-order_date')
