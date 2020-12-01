from datetime import datetime
import uuid
from django.db import models
from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
from django.utils.html import mark_safe

category = [
    ('album', 'Album'),
    ('news', 'Noticia'),
    ('opinion', 'Articulo'),
    ('event', 'Evento'),
    ('song', 'Cancion'),
    ]
class BaseMeta(models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class Publication(BaseMeta):
    title = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=2000, null=False)
    image = models.ImageField()
    category = models.CharField(max_length=255,choices=category)
    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

class Artist(BaseMeta):
    name = models.CharField(max_length=255, null=False)
    spotify = models.CharField(max_length=2000, null=True)
    youtube = models.CharField(max_length=2000, null=True)
    web = models.CharField(max_length=2000, null=True)
    image = models.ImageField()

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))
    def __str__(self):
        return self.name

    image_tag.short_description = 'Image'


class Album(BaseMeta):
    name = models.CharField(max_length=255, null=False)
    artist = models.ForeignKey(Artist, blank=True, null=True, on_delete=models.SET_NULL)
    spotify = models.CharField(max_length=2000, null=True)
    image = models.ImageField()

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))
    def __str__(self):
        return self.name

    image_tag.short_description = 'Image'

class Song(BaseMeta):
    name = models.CharField(max_length=255, null=False)
    album = models.ForeignKey(Album, blank=True, null=True, on_delete=models.SET_NULL)
    artist = models.ForeignKey(Artist, blank=True, null=True, on_delete=models.SET_NULL)
    spotify = models.CharField(max_length=2000, null=True)
    youtube = models.CharField(max_length=2000, null=True)
    image = models.ImageField()

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

    def __str__(self):
        return self.name

    image_tag.short_description = 'Image'
    #ADICIONAR DISQUERA

class Pop30(BaseMeta):
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    count = models.PositiveIntegerField(default=0)
    spotify = models.CharField(max_length=2000, null=True,blank=True)
    youtube = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField()

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'

    @classmethod
    def get_next(cls):
        cls.objects.update(count=models.F('count') + 1)
        return cls.objects.values_list('count', flat=True)[0]

class Poporder(BaseMeta):
    pop30 = models.ForeignKey(Pop30, blank=True, null=True, on_delete=models.SET_NULL)
    song = models.ForeignKey(Song, blank=True, null=True, on_delete=models.SET_NULL)
    position = models.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(30)])

