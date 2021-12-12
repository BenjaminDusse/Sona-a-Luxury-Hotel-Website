from django.shortcuts import render, get_object_or_404, redirect

from .forms import SearchForm
from .models import Service, Category, Rating_Star, Room, Comment, Gallery
from blog.models import Post


def search(request):
    if request.method == 'POST':
        form.save()
        return redirect('res_system:')

    context = {
        'form': form
    }

    return render(request, 'res_system/search.html', context)



def home(request):
    categories = Category.objects.all()
    rating_stars = Rating_Star.objects.all()
    rooms = Room.objects.all().order_by('-date_created')
    comments = Comment.objects.all()
    services = Service.objects.all()
    posts = Post.objects.all().order_by('date_posted')

    context = {
        'categories': categories,
        'rating_stars': rating_stars,
        'rooms': rooms[:4],
        'posts': posts[:5],
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
        'comments': comments,
        'services': services[:2]
    }
    return render(request, 'res_system/room_list.html', context)


def room_detail(request, slug):
    room = get_object_or_404(Room, slug=slug)

    context = {
        'room': room
    }
    return render(request, 'res_system/room_detail.html', context)


def about(request):
    context = {}
    return render(request, 'res_system/about.html', context)

def contact(request):
    context = {}
    return render(request, 'res_system/contact.html', context)



