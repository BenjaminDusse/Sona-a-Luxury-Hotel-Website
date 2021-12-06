from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='blog/post_images/')
    tagline_images = models.ImageField(upload_to="blog/post_images/tagline_images")
    tags = models.ManyToManyField(Tag, related_name='posts')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Rating_Star(models.Model):
    star = models.PositiveIntegerField()
    star_icon = models.ImageField(upload_to='rooms/rating_stars')



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    rating_stars = models.ForeignKey(Rating_Star, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f"{ self.author.username }' comment"


# create shared links for detail page blog add any logic
# add likes and dislikes into rooms and blog detail comments
# for siklida har xil stilda chiqadigan qilib sikl yaratish