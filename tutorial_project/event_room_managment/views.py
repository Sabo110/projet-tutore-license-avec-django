from django.shortcuts import render

def home_page(request):
    return render(request, 'event_room_managment/home_page.html')
