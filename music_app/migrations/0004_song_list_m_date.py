# Generated by Django 3.0.2 on 2021-11-22 09:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0003_auto_20211119_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='song_list_m',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]