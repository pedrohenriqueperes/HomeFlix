from django.contrib import admin
from django.urls import path
from .views import *






urlpatterns = [
    path('', home, name='home'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('protagonist/<str:protagonist_name>/', protagonist_detail, name='protagonist_detail'),
]