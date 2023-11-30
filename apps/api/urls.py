from django.urls import path
from .views import products

urlpatterns = [
    path("products", products.ProductApiView.as_view()),
    path("products/<str:product_id>", products.ProductDetailApiView.as_view())
]
