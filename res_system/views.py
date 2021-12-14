from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail


from .forms import SubscribersForm, MailMessageForm
from .models import Service, Category, Rating_Star, Room, Comment, Gallery
from blog.models import Post


def mail_letter(request):

    mail_message = MailMessageForm()

    if request.method == 'POST':
        mail_message = MailMessageForm(request.POST)
        if mail_message.is_valid():
            mail_message.save()
            name = mail_message.cleaned_data.get('name')
            email = mail_message.cleaned_data.get('email')
            message = mail_message.cleaned_data.get('message')
            send_mail(
                name,
                message,
                '',
                ['fazliddinabduhakimov9@gmail.com',
                    'abduhakimovfazliddin2002@gmail.com'],
                fail_silently=False
            )
            messages.success(
                request, 'Message has been sent to the site owners!')

    context = {
        'mail_message': mail_message
    }
    return render(request, 'res_system/mail_letter.html', context)


def search(request):

    if request.method == 'POST':
        searched = request.POST['searched']
        rooms = Room.objects.filter(name__icontains=searched)


    context = {
        'searched': searched,
        'rooms': rooms
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

    mail_form = MailMessageForm()

    if request.method == 'POST':
        mail_form = MailMessageForm(request.POST)
        if mail_form.is_valid():
            mail_form.save()
            messages.success(
                request, "We take your message. We'l connect with you in a short time")
            return redirect('res_system:contact')
        else:
            mail_form = MailMessageForm()

    context = {
        'mail_form': mail_form
    }
    return render(request, 'res_system/contact.html', context)
