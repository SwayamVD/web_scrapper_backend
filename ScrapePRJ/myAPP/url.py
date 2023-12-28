# myapp/urls.py
from django.urls import path
from .views import get_amazon_data

urlpatterns = [
    path('api/get_amazon_data/<path:product_url>/', get_amazon_data, name='get_amazon_data'),
]
