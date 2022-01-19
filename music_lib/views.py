from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

def index(request):
    albums = Album.objects.all()
    return render(request, 'albums/home.html', {'albums': albums})

def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            new_album = form.save()
            return redirect("home")

    else:
        form = AlbumForm()
    return render (request, 'albums/add_album.html', {'form': form})


