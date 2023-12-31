# Generated by Django 4.2.7 on 2023-11-29 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("musics", "0006_alter_favorite_music"),
    ]

    operations = [
        migrations.AddField(
            model_name="song",
            name="loader",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="loader",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="favorite",
            name="music",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favoritemusic",
                to="musics.song",
            ),
        ),
        migrations.DeleteModel(
            name="MusicFile",
        ),
    ]
