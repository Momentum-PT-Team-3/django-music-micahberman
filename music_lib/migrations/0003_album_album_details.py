# Generated by Django 4.0 on 2022-01-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_lib', '0002_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_details',
            field=models.TextField(null=True),
        ),
    ]