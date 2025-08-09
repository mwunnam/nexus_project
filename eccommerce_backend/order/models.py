from django.db import models
from django.contrib.auth import get_user_model
from catalog.models import Product
from customer.models import Customer

User = get_user_model()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'Oder {self.pk} by {self.customer}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['product'])
        ]

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

