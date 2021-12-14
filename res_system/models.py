from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


from PIL import Image



class Service(models.Model):
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
    star_icon = models.ImageField(upload_to='rooms/rating_stars', blank=True, null=True)

    def __str__(self):
        return str(self.star)


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
    services = models.ManyToManyField(Service, related_name='room')
    content = RichTextField()
    rating_stars = models.ForeignKey(Rating_Star, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.PositiveIntegerField(default=15)
    capacity_persons = models.PositiveIntegerField(default=2)
    check_in = models.DateTimeField(default=timezone.now)
    check_out = models.DateTimeField(default=timezone.now, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now, null=True)
    slug = models.SlugField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    

    def __str__(self):
        return f"{self.name} room"

    def get_absolute_url(self):
        return reverse('res_system:room_detail', args=[str(self.slug)])


    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 233.5:
            output_size = (750, 423)
            img.thumbnail(output_size)
            img.save(self.image.path)
        


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    rating_stars = models.ForeignKey(Rating_Star, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{ self.author.username } {self.content}"


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title


class Subscribers(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.email


class MailMessage(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.name} - {self.message}"







