from rest_framework import serializers
from .models import Order, OrderItem
from customer.models import Customer
from catalog.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.ReadOnlyField(source='product.name') 

    class Meta:
        model = OrderItem
        fields = ['id','product', 'product_name', 'quantity']


class OrderSerialiazer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True) 

    class Meta:
        model = Order
        fields = ['id', 'customer', 'created_at', 'is_paid', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

