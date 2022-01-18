from django.db import models
from django.utils import timezone

class Categories_m(models.Model):
    Category = models.SlugField("new Category", primary_key = True, null = False, blank = False)
    def __str__(self):
        return self.Category

class Tags_m(models.Model):
    tag = models.SlugField(primary_key = True, null = False, blank = False)
    def __str__(self):
        return self.tag

class Song_list_m(models.Model):
    ID = models.CharField("Youtube ID", primary_key = True, null = False, blank = False, max_length = 30)
    Title = models.CharField(max_length = 50)
    Category = models.ForeignKey(Categories_m, on_delete = models.PROTECT)
    Alter_ID = models.CharField("Alternate Youtube ID", max_length = 30, blank = True)
    DM_ID = models.CharField("DailyMotion ID", max_length = 30, blank = True)
    SC_ID = models.CharField("SoundCloud ID", max_length = 100, blank = True)
    Time = models.FloatField(default = 0.0) 
    Rating = models.IntegerField(default = 0)
    Date = models.DateTimeField(auto_now_add = True) 
    default_id = models.IntegerField(default = 1)
    Tags = models.ManyToManyField(Tags_m)
    def __str__(self):
        return self.Title

