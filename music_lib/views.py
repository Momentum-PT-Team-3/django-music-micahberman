from ast import Delete
from django.shortcuts import render, redirect, get_object_or_404
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

def album_details(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render (request, 'albums/album_details.html', {'album': album})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance = album) 
        if form.is_valid():
            album = form.save() 
            return redirect ('album_details', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/album_edit.html', {'album' : album, 'form' : form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        album.delete()
        return redirect ('home')
    return render(request, 'albums/album_delete.html', {'album' : album})
