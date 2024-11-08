from tkinter.font import names

from django.contrib import admin
from django.urls import path
from .views import *






urlpatterns = [
    path('', home, name='home'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
]