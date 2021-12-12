from django.urls import path
from . import views


app_name="blog"
urlpatterns = [
    path("", views.blog_list, name="blog_list"),
    path("<slug:slug>/<int:pk>/", views.blog_detail, name="blog_detail"),

    path('like/<int:pk>/', views.like_post, name="like_post"),
    path('dislike/<int:pk>/', views.dislike_post, name="dislike_post"),
]