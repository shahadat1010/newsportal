from django.http.response import HttpResponse
from django.shortcuts import render
from newsapp.models import  Author, Category,Post 

# Create your views here.

def home(request):
    #load all the post from db(10)
    posts = Post.objects.all()
    #print(posts)
    cats = Category.objects.all()
    data = {
        'posts': posts,
        'cats': cats 
    }
    return render(request,'home.html',data)

def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    #print(post)
    return render(request, 'posts.html',{'post': post,'cats':cats})

def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,"category.html", {'cat':cat,'posts':posts})

def author(request):
    authors = Author.objects.all()
    data = {'authors':authors}
    return render(request,'author.html', data)

def about(request):
    return render(request,"about.html",{})



