from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Song(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    artist = models.CharField(max_length=200,  verbose_name="Исполнитель")
    image = models.ImageField(blank=True, null=True, upload_to="img", default="default.jpg",  verbose_name="Обложка(необязательно)")
    audio_file = models.FileField(null=True, upload_to="audio", verbose_name="Аудио файл")
    loader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loader", null=True, verbose_name="Пользователь, который загрузил файл")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'


class Favorite(models.Model):
    music = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="favoritemusic", null=True, verbose_name="Песня")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favoriteuser", verbose_name="Пользователь")

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'



class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'artist', 'image', "audio_file"]


