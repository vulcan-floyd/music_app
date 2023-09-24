from django.forms import ModelForm
from .models import Song, Artist, Genre

class SongUploadForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'description', 'thumbnail', 'artist', 'audio', 'genre']
        
class ArtistUploadForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'slug', 'bio', 'country', 'thumbnail']
        
class GenreUploadView(ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'thumbnail']
