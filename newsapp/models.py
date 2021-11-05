from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField
from django.utils.html import  format_html





# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    def image_tag(self):
        return format_html('<img src=" /media/{}" style="width:40px;height:40px;border-radius:50%;" /> '.format(self.image))
    
    def __str__(self):
        return self.title


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    
    

    def image_post(self):
        return format_html('<img src ="/media/{}" style ="width:40px;height:40px;border-radius:50%;"/>'.format(self.image))
    
    
    def __str__(self):
        return self.post_title

class Author(models.Model):
   display_name = models.CharField(max_length=15)
   email = models.EmailField(max_length=20)
   password = models.CharField(max_length=20)
   profile_picture = models.ImageField(upload_to='profile_image', blank=True)
   blog = models.TextField(default=" ")
   url = models.CharField(max_length=100)

   def image_tag(self):
        return format_html('<img src=" /media/{}" style="width:40px;height:40px;border-radius:50%;" /> '.format(self.profile_picture))
    
   def __str__(self):
        return self.display_name   

