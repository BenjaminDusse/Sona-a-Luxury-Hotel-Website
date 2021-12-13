from django.urls import path
from . import views


app_name="res_system"
urlpatterns = [
    path("", views.home, name="home"),
    path("rooms/", views.room_list, name="room_list"),
    path("rooms/<slug:slug>/", views.room_detail, name="room_detail"),

    path("about/", views.about, name='about'),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    
]