from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def cart(request):
    return render(request, 'pages/cart.html')

def order(request):
    return render(request, 'pages/order.html')

def thankyou(request):
    return render(request, 'pages/thankyou.html')