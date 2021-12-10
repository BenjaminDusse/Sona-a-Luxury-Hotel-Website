from django.contrib import admin
from .models import Tag, Post, Rating_Star, Comment, Category


admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Rating_Star)
admin.site.register(Category)