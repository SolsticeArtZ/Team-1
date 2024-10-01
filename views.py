from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import User

# Create your views here.
def index(request):
    Product_list = Product.objects.all()
    return render(request, 'index.html', {'products': Product_list})

def new_user(request):
    return render(request, 'newuser.html')