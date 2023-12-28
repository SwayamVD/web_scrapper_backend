# myapp/views.py
from django.http import JsonResponse
from .amazon import scrape_amazon

def get_amazon_data(request,product_url):
    url = "https://www.amazon.com/example-product-url"  # Replace with your specific product URL
    data = scrape_amazon(product_url)
    return JsonResponse(data=data)
