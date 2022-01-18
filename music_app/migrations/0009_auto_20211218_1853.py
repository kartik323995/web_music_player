# Generated by Django 3.0.2 on 2021-12-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0008_auto_20211125_1654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags_m',
            fields=[
                ('tag', models.SlugField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='song_list_m',
            name='Tags',
            field=models.ManyToManyField(to='music_app.Tags_m'),
        ),
    ]
