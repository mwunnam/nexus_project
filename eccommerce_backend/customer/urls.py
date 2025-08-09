from django.urls import path
from .views import CustomerListCreateView, CustomerOrdersView

urlpatterns = [
    path('', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('<int:customer_id>/', CustomerOrdersView.as_view(), name='customer-orders')
]
