# Generated by Django 4.0.1 on 2022-01-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_lib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('artist', models.CharField(blank=True, max_length=100, null=True)),
                ('creation_time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
