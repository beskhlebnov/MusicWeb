# Generated by Django 4.2.7 on 2023-11-29 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musics", "0004_musicfile_created_on_alter_musicfile_mfile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Song",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField()),
                ("artist", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                ("audio_file", models.FileField(blank=True, null=True, upload_to="")),
                ("audio_link", models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]