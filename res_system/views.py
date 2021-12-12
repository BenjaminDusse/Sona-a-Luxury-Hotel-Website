from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import SearchForm, SubscribersForm
from .models import Service, Category, Rating_Star, Room, Comment, Gallery
from blog.models import Post


def newsletter(request):
    newsletter_form = SubscribersForm()
    
    context = {
        'newsletter_form': newsletter_form
    }
    return render(request, 'res_system/mail.html')


def search(request):
    search_form = SearchForm()
    if request.method == 'POST':
        if search_form.is_valid():
            search_form.save()
            return redirect('/')
        
    context = {
        'search_form': search_form
    }

    return render(request, 'res_system/search.html', context)



def home(request):
    categories = Category.objects.all()
    rating_stars = Rating_Star.objects.all()
    rooms = Room.objects.all().order_by('-date_created')
    comments = Comment.objects.all()
    services = Service.objects.all()
    posts = Post.objects.all().order_by('date_posted')
    newsletter_form = SubscribersForm()

        
    if request.method == 'POST':
        newsletter_form = SubscribersForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, 'Subscription accepted!')
            return redirect('/')
        else:
            newsletter_form = SubscribersForm()

    context = {
        'categories': categories,
        'rating_stars': rating_stars,
        'rooms': rooms[:4],
        'posts': posts[:5],
        'comments': comments,
        'newsletter_form': newsletter_form,
        
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



