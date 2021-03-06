from django.contrib import admin
from .models import Service, Category, Rating_Star, Room, Comment, Gallery, Subscribers, MailMessage
# Register your models here.

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Room)
admin.site.register(Comment)
# admin.site.register(Gallery)
admin.site.register(Subscribers)
admin.site.register(MailMessage)

class Rating_StarAdmin(admin.ModelAdmin):
    model = Rating_Star
    list_display = ['star']
    


admin.site.register(Rating_Star, Rating_StarAdmin)