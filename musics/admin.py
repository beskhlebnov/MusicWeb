from django.contrib import admin
from .models import Favorite, Song


class FavoriteAdmin(admin.ModelAdmin):
    title = ['id', 'music', 'user']
    search_fields = ['music__title', 'user__username']
    list_filter = ['music', 'user']
    list_display = ['id','music', 'user']
    editable_list = ['music', 'user']


class SongAdmin(admin.ModelAdmin):
    title = ['id', 'title', 'artist', "image", "audio_file", "loader"]
    search_fields = ['title', 'artist', "loader__username"]
    list_filter = ['title', 'artist', "loader"]
    list_display = ['id', 'title', 'artist', "image", "audio_file", "loader"]
    editable_list = ['title', 'artist', "image", "audio_file", "loader"]


admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Song, SongAdmin)