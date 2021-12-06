from django.contrib import admin
from .models import Services, Category, Rating_Star, Room, Comment, Gallery  
# Register your models here.

admin.site.register(Services)
admin.site.register(Category)
admin.site.register(Rating_Star)
admin.site.register(Room)
admin.site.register(Comment)
admin.site.register(Gallery)