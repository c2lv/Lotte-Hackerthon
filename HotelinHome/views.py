from django.shortcuts import render
from django import forms

def index(request):
    return render(request, 'index.html')
