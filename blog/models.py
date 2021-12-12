from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    content = RichTextField()
    image = models.ImageField(upload_to='blog/post_images/')
    tagline_images = models.ImageField(upload_to="blog/post_images/tagline_images", blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='posts')
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    dislikes =models.ManyToManyField(User, related_name='post_dislikes', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)       


    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[str(self.slug), str(self.pk)])


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