# Generated by Django 3.0.2 on 2021-11-18 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories_m',
            fields=[
                ('Category', models.SlugField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Song_list_m',
            fields=[
                ('ID', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Alter_ID', models.CharField(max_length=30)),
                ('DM_ID', models.CharField(max_length=30)),
                ('SC_ID', models.CharField(max_length=30)),
                ('Time', models.FloatField()),
                ('Rating', models.IntegerField(default=0)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='music_app.Categories_m')),
            ],
        ),
    ]
