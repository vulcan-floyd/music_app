# Generated by Django 4.2.2 on 2023-06-21 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_artist_id_song_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(default='blank-profile-picture.png', upload_to='albums')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.artist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.song')),
            ],
        ),
    ]
