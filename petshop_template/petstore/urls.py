from django.urls import path
from products.views import get_products, index, delete_product, add_products

urlpatterns = [
    path('', index, name='index'),
    path('api/products/', get_products, name='get-products'),
    path('add_products/', add_products, name='add_products'),
path('api/products/<str:id>/delete/', delete_product, name='delete_product'),
]
