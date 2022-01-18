from django.contrib import admin
from .models import Categories_m, Song_list_m, Tags_m

admin.site.register(Categories_m)
admin.site.register(Song_list_m)
admin.site.register(Tags_m)