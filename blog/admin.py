from django.contrib import admin
from django.db import models
from .models import Blog
from tinymce.widgets import TinyMCE
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title / Date", {'fields' : ['blog_title', 'blog_published']}),
        ("Content", {"fields" : ["blog_content"]})
    ]

    formfield_overrides = {
        models.TextField : {'widget' : TinyMCE()}
    }
admin.site.register(Blog, BlogAdmin)