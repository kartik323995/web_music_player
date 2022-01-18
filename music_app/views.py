from django.shortcuts import render, redirect, get_object_or_404
from .models import Categories_m, Song_list_m, Tags_m
from .forms import Song_list_f, Categories_f 
from django.core import serializers
from django.http import JsonResponse, HttpResponse

def home(request):
    return categories(request, 'All')

def add_new(request):
    if request.method == 'POST':
        form = Song_list_f(request.POST)
        form_c = Categories_f(request.POST)     
        if form_c.is_valid():
            form_c.save()
            return redirect('add_new')  
        if form.is_valid():
            form.save()
            return redirect('add_new')
    else: 
        form = Song_list_f() 
        form_c = Categories_f()     
    return render(request, 'music_app/add_new.html', {'form': form, 'form_c': form_c})

def categories(request, category_v):
    categories = Categories_m.objects.all()
    if category_v == 'All':
        song_list = Song_list_m.objects.all().order_by('-Date')
    else:
        obj = get_object_or_404(Categories_m, Category = category_v)
        song_list = Song_list_m.objects.filter(Category = obj).order_by('-Date')
    tags_l = []
    for song in song_list:
        s = ";"
        for tag in song.Tags.all():
            s += tag.tag+";"
        tags_l.append(s)
    return render(request, 'music_app/home.html', {'categories': categories,
                 'song_list': song_list, 'category':category_v, 'tags':tags_l, 'form': Song_list_f()})

def ajax_update(request):
    obj = Song_list_m.objects.get(ID = request.GET["ID"])
    if obj == None:
        message = "Not Updated"
    else:
        form = Song_list_f(request.GET, instance = obj)
        if form.is_valid():
            form.save()
            message = "success"
        else:
            message = "Not Updated"
    return HttpResponse(message)

def ajax_song_delete(request):
    obj = Song_list_m.objects.get(ID = request.GET["ID"])
    if obj != None:
        obj.delete()
        message = "success"
    else:
        message = "Not deleted"
    return HttpResponse(message)

def ajax_category_delete(request):
    obj = Categories_m.objects.get(Category = request.GET['Category'])
    if obj != None:
        obj.delete()
        message = "success"
    else:
        message = "Fail"
    return HttpResponse(message)



  
