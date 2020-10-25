from django.shortcuts import render
from django import forms

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')    

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')
    
def menu(request):
    return render(request, 'menu.html')
        
def reservation(request):
    return render(request, 'reservation.html')

def stuff(request):
    return render(request, 'stuff.html')

def yeo(request):
    return render(request, 'yeo_kyungok.html')

def yannick(request):
    return render(request, 'yannick_alleno.html')

def pierre(request):
    return render(request, 'pierre_gagnaire.html')

def cheon(request):
    return render(request, 'cheon_deoksang.html')

    
    