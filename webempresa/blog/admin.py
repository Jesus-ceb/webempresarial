from django.contrib import admin
from .models import Category, Post


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('title', 'author', 'published')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)