# Generated by Django 4.0.6 on 2022-07-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_alter_song_options_song_album_alter_song_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover_image', models.URLField()),
                ('slug_field', models.SlugField(unique=True)),
            ],
        ),
    ]
