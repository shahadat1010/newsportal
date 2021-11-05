from django.contrib import admin
from django.urls import path

from .views import home,post,category,author
from newsapp import views 

urlpatterns = [

    path('home/',home),
    path('newsapp/<slug:url>',post),
    path('category/<slug:url>',category),
    path('author/',author ),
    path('about/',views.about),
    
       
] 
