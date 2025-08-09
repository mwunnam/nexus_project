from django.urls import path
from .views import (
    CategoryListCreateView, CategoryRetrieveUpdateDestroyView, ProductListCreateView, ProductRetrieveUpdateDestroyView
)

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='categories-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('products/', ProductListCreateView.as_view(), name='products=list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='prouduct-detail'),
]
