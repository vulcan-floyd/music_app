from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('artist', views.ArtistView.as_view(), name='artist'),
    path('genres', views.GenreView.as_view(), name='genre'),
    path('song', views.SongView.as_view(), name='song'),
    path('song/upload', views.SongUploadView.as_view(), name='upload_song'),
    path('artist/upload', views.ArtistUploadView.as_view(), name='upload_artist'),
    path('genre/upload', views.GenreUploadView.as_view(), name='upload_genre'),
    path('artist/<slug:slug>', views.ArtistSlugView.as_view(), name="artist_slug")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    