# Generated by Django 4.2.2 on 2023-06-19 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_artist_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song',
            new_name='audio',
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
