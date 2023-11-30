from django.urls import path
from .views import product, category, status

urlpatterns = [
    path("products", product.ProductApiView.as_view()),
    path("products/<str:product_id>", product.ProductDetailApiView.as_view()),
    path("statuses", status.StatusAPIView.as_view()),
    path("categories", category.CategoryAPIView.as_view()),
]