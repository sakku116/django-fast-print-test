from django.shortcuts import render
from api.models import Product, Category, Status

# Create your views here.
def index(request):
    return render(request, 'index.html')