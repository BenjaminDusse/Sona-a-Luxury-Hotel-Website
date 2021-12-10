from django.shortcuts import render, get_object_or_404
from .models import Service, Category, Rating_Star, Room, Comment, Gallery



def home(request):
    categories = Category.objects.all()
    rating_stars = Rating_Star.objects.all()
    rooms = Room.objects.all() 
    comments = Comment.objects.all()
    services = Service.objects.all()

    context = {
        'categories': categories,
        'rating_stars': rating_stars,
        'rooms': rooms,
        'comments': comments
    }
    return render(request, 'res_system/home.html', context)




def room_list(request):
    categories = Category.objects.all()
    rating_stars = Rating_Star.objects.all()
    rooms = Room.objects.all().order_by('-date_created')
    comments = Comment.objects.all()
    services = Service.objects.all()


    context = {
        'categories': categories,
        'rating_stars': rating_stars,
        'rooms': rooms,
        'comments': comments
    }
    return render(request, 'res_system/room_list.html', context)


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)

    context = {
        'room': room
    }
    return render(request, 'res_system/room_detail.html', context)


