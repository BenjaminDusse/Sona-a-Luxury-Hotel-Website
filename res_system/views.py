from django.shortcuts import render



def home(request):
    context = {}
    return render(request, 'res_system/home.html')

def room_list(request):
    context = {}
    return render(request, 'res_system/room_list.html', context)