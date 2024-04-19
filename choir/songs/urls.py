from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('filter/', views.filter_songs, name='filter_songs'),
     path('download/<int:song_id>/', views.download_song, name='download_song'),
      path('upload/', views.upload_song, name='upload_song')
]
