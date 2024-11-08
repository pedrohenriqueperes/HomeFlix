# views.py
from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import Max


def home(request):
    movies = Movie.objects.all().order_by('-upload_date')

    # Busca protagonistas com fotos de forma compatível com SQLite
    protagonists = (Movie.objects
                    .exclude(protagonist_image='')
                    .values('protagonist', 'protagonist_image')
                    .distinct())

    context = {
        'movies': movies,
        'protagonists': protagonists,
    }

    return render(request, 'index.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})