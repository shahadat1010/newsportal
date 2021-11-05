from django.contrib import admin
from .models import  Category,Post,Author

# Register your models here.
#for configuration of Category
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('title', 'add_date','image_tag' )
     search_fields = ('title',)
     

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'url','add_date','image_post') 
    search_fields = ('post_title',)
    list_filter = ('cat',)
    list_per_page = 50
    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js', 'js/script.js',)
        
class AuthorAdmin(admin.ModelAdmin):
    list_display=('display_name','image_tag','url')   
    search_fields=('display_name',)
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorAdmin)
