from django.contrib import admin
from api.models import Publication
from api.models import Artist
from api.models import Album
from api.models import Song
from api.models import Pop30
from api.models import Poporder
from django.utils.html import format_html


class PublicationAdmin(admin.ModelAdmin):

    model = Publication
    list_display =  ('id',
    'title',
    'content',
    'image_tag','category', 'created_at', 'updated_at' )
    readonly_fields = ['created_at', 'updated_at']

class ArtistAdmin(admin.ModelAdmin):

    model = Artist
    list_display = ['id',
    'name',
    'image_tag',
    'spotify_url',
    'youtube_url' ,
    'web_url',
    'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

    def spotify_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.spotify)
    def youtube_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.youtube)
    def web_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.web)

class AlbumAdmin(admin.ModelAdmin):

    model = Album
    list_display = ('id',
    'name',
    'image_tag',
    'artist',
    'spotify_url'
    , 'created_at', 'updated_at')
    readonly_fields = ['created_at', 'updated_at']

    def spotify_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.spotify)


class SongAdmin(admin.ModelAdmin):
    model = Song
    list_display = ('id',
    'name',
    'artist',
    'image_tag',
    'spotify',
    'youtube' ,
     'created_at', 'updated_at',
     )
    readonly_fields = ['created_at', 'updated_at']

class PoporderInline(admin.StackedInline):
    model = Poporder
    extra = 1
    readonly_fields = ('created_at', 'updated_at')


class Pop30Admin(admin.ModelAdmin):

    model = Pop30
    list_display = ('id',
    'count',
    'image_tag',
                    'start_date',
    'end_date',
    'spotify' ,
    'youtube'  ,

    'created_at', 'updated_at',)
    inlines = [PoporderInline]
    readonly_fields = ['created_at', 'updated_at']




admin.site.register(Publication,PublicationAdmin)
admin.site.register(Artist,ArtistAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(Song,SongAdmin)
admin.site.register(Pop30,Pop30Admin)
