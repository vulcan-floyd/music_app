import math
import datetime

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    slug = models.SlugField(unique=True)
    bio = models.TextField()
    country = models.CharField(max_length=50, null=False, default=None)
    thumbnail = models.ImageField(upload_to='artist_image', default='blank-profile-picture.png')
    
    class Meta:
        db_table = 'core_artist'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

class Genre(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    thumbnail = models.ImageField(upload_to='genres', default='blank-profile-picture.png')
    
    def __str__(self):
        return self.name

class Song(models.Model):

    title = models.CharField(max_length=50, null=False, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='song_images', default='blank-profile-picture.png', blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='songs')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
        # return reverse("_detail", kwargs={"pk": self.pk})

    # @property
    # def file_size(self):
    #     if self.size == 0:
    #         return "0B"
    #     size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    #     i = int(math.floor(math.log(self.size, 1024)))
    #     p = math.pow(1024, i)
    #     s = round(self.size / p, 2)
    #     return "%s %s" % (s, size_name[i])
    
class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="albums", default='blank-profile-picture.png', blank=False)
