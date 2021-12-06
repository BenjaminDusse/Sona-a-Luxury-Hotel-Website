from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Services(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='service_icons', blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='category_icons', blank=True, null=True)


    def __str__(self):
        return self.name



class Rating_Star(models.Model):
    star = models.PositiveIntegerField()
    star_icon = models.ImageField(upload_to='rooms/rating_stars')



class Room(models.Model):
    type_choices = (
        ('Pernight', 'Pernight'),
        ('For Week', 'For Week'),
        ('For three days', 'For three days'),
        ('How you want', 'How you want')
    )
    bed_choices = (
        ('King Beds', 'King Beds'),
        ('Special for you', 'Special for you'),
        ('Italian furniture', 'Italian furniture'),
        ('How you want', 'How you want')
    )


    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='rooms_pics')
    room_type = models.CharField(max_length=200, choices=type_choices)
    bed_type = models.CharField(max_length=200, choices=bed_choices)
    services = models.ManyToManyField(Services, related_name='room')
    content = RichTextField()
    rating_stars = models.ForeignKey(Rating_Star, on_delete=models.SET_NULL, null=True, blank=True)
    size_in_ft = models.PositiveIntegerField(default=15)
    capacity_persons = models.PositiveIntegerField(default=2)


    def __str__(self):
        return f"{self.name} room"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    rating_stars = models.ForeignKey(Rating_Star, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{ self.author.username }' comment"


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title
    
# rating star yaratish 5 xilini va iconlarini css dan topish yoki svg xullas