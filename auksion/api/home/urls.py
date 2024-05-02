from django.urls import path, include
from .views import ProductListView, ProductSingleView, CreateProductView
urlpatterns = [
    path('product_list/', ProductListView.as_view()),
    path('single_product/', ProductSingleView.as_view()),
    path('creat_product/', CreateProductView.as_view())
]