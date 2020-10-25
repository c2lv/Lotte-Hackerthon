from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.
def review(request):
    posts = Post.objects.all()
    return render(request, 'posts/review.html',{'posts':posts})

def reviewadd(request):
    return render(request, 'posts/review_add.html')


def reviewedit(request, id):
    post=get_object_or_404(Post,pk=id)
    if request.method=="POST":
        post.chef=request.POST['chef']    
        post.content=request.POST['content']
        post.menu=request.POST['menu']
        post.image=request.FILES.get('image')
        post.save()
        return redirect('posts:review')
    return render(request, 'posts/review_edit.html', {"post":post})


def create(request):
   if  request.method == "POST":
        chef = request.POST.get('chef')
        menu = request.POST.get('menu')
        content = request.POST.get('content')
        image=request.FILES.get('image')
        Post.objects.create(chef=chef, menu=menu, content=content, image=image)
        return redirect('posts:review')

def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('posts:review')    