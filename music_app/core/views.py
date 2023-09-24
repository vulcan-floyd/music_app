from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseBadRequest

from .models import Song, Artist, Genre
from .forms import SongUploadForm, ArtistUploadForm, GenreUploadView

import datetime

# Create your views here.
# class HomePage(View):
#     @login_required
#     def get(self, request):
#         # return render(request, 'index.html')
#         return HttpResponse("Home Page")


class HomePage(View):
    template_name = 'home.html'
    
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        today = datetime.datetime.now()
        week_ago = today - datetime.timedelta(days=7)
        latest_song = Song.objects.filter(created_at__gte=week_ago)
        genre = Genre.objects.all()
        artists = Artist.objects.all()
        context = {
            "latest_songs": latest_song,
            "genres": genre,
            "artists": artists
        }
        # return HttpResponse("Home Page")
        return render(request, HomePage.template_name, context=context)

class SongView(View):
    pass

class ArtistUploadView(View):
    template_name = 'forms/artist_form.html'
    
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        # form = ArtistUploadForm()
        artists = Artist.objects.all()
        print(artists)
        # context = {
        #     "artists": artists
        # }
        return render(request, ArtistUploadView.template_name)
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        country = request.POST['country']
        bio = request.POST['bio']
        # slug = request.POST['slug']
        thumbnail = request.FILES['thumbnail']
        artist = Artist.objects.filter(name=name)
        if not artist:
            artist = Artist(name=name,
                            country=country,
                            bio=bio,
                            thumbnail=thumbnail)
        else:
            Artist.objects.filter(name=name).update(name=name,
                        country=country,
                        bio=bio,
                        thumbnail=thumbnail)
        
        try:
            artist.save()
        except Exception as e:
            print(e)
            return HttpResponseBadRequest("INvalid Artist")
        return HttpResponse("Artist Uploaded Successfully")
    
class GenreUploadView(View):
    template_name = 'forms/genre_form.html'
    
    @method_decorator(login_required)
    def get(self, request):
        # form = GenreUploadView()
        all = Genre.objects.all()
        print(all)
        return render(request, GenreUploadView.template_name)
    
    @method_decorator(login_required)
    def post(self, request):
        name = request.POST['name']
        thumbnail = request.FILES['thumbnail']
        genre = Genre.objects.filter(name=name)
        if not genre:
            genre = Genre(name=name,
                        thumbnail=thumbnail)
            try:
                genre.save()
            except Exception as e:
                print(e)
                return HttpResponseBadRequest("Invalid Genre")
        else:
            Genre.objects.filter(name=name).update(name=name,
                                                   thumbnail=thumbnail)

        return HttpResponse("Genre Uploaded Successfully")

class SongUploadView(View):
    template_name = 'forms/song_form.html'
    
    @method_decorator(login_required)
    def get(self, request):
        # form = SongUploadForm()
        # print(form)
        # context = {
        #     'form': form
        # }
        all = Genre.objects.all()
        print(all)
        return render(request, SongUploadView.template_name)
    
    @method_decorator(login_required)
    def post(self, request):
        title = request.POST['title']
        description = request.POST['description']
        thumbnail = request.FILES['thumbnail']
        artist_name = request.POST['artist']
        audio = request.FILES['song']
        genre_name = request.POST['genre']
        try:
            artist = Artist.objects.get(name=artist_name)
        except Exception as e:
            return HttpResponseBadRequest("Artist Not Created, Please Create an Artist First")
        
        try:
            genre = Genre.objects.get(name=genre_name)
        except Exception as e:
            return HttpResponseBadRequest("Genre Not Created, Please Create an Genre First")
        
        song = Song.objects.filter(title=title)
        if not song:
            song = Song(title=title,
                        description=description,
                        thumbnail=thumbnail,
                        artist=artist,
                        audio=audio,
                        genre=genre)
            try:
                song.save()
            except Exception as e:
                print(e)
                return HttpResponseBadRequest("Invalid Song")
        else:
            Song.objects.filter(title=title).update(title=title,
                                                    description=description,
                                                    thumbnail=thumbnail,
                                                    artist_name=artist,
                                                    song=song,
                                                    genre=genre)

        return HttpResponse("Song Uploaded Successfully")
    
class AlbumView(View):
    pass

class ArtistView(View):
    template_name = 'artists/index.html'
    
    def get(self, request, *args, **kwargs):
        artists = Artist.objects.all()
        context = {
            "artists": artists
        }
        return render(request, ArtistView.template_name, context=context)
    
class ArtistSlugView(View):
    model = Artist
    template_name = 'artist/show.html'
    
    def get(self, request, *args, **kwargs):
        slug_value = kwargs['slug']
        return HttpResponse("artist-")

class GenreView(View):
    pass