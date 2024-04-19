from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import SongForm


# Create your views here.

from .models import Song


def index(request):
    query = request.GET.get('q')
    if query:
        songs = Song.objects.filter(title__icontains=query)
    else:
        songs = Song.objects.all()

    form = SongForm()
    return render(request, 'songs/index.html', {'songs': songs, 'form': form})


def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SongForm()
    
    return render(request, 'songs/upload_song.html', {'form': form})


def filter_songs(request):
    file_type = request.GET.get('file_type')
    if file_type:
        songs = Song.objects.filter(file_type=file_type)
    else:
        songs = Song.objects.all()
    
    return render(request, 'songs/index.html', {'songs': songs})


def download_song(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    song_file = open(song.file.path, 'rb')
    response = HttpResponse(song_file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{song.file.name}"'
    return response