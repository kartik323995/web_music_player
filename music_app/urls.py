from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('new/', views.add_new, name = 'add_new'),
    path('<slug:category_v>/', views.categories, name = 'categories'),
    path('ajax/update/', views.ajax_update, name = 'update'),
    path('ajax/delete/song/', views.ajax_song_delete, name = 'song_delete'),
    path('ajax/delete/category/', views.ajax_category_delete, name = 'category_delete'),
]