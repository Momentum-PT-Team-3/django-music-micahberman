from django.shortcuts import render
from .models import Album

def index(request):
    albums = Album.objects.all()
    return render(request, 'albums/home.html', {'albums': albums})
