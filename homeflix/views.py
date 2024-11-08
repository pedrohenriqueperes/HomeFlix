from django.shortcuts import render, get_object_or_404
from .models import Movie, Protagonist
from django.db.models import Max


def home(request):
    # Get all movies ordered by upload date
    movies = Movie.objects.all().order_by('-upload_date')

    # Get all protagonists with their images
    protagonists = Protagonist.objects.exclude(image='').distinct()

    context = {
        'movies': movies,
        'protagonists': protagonists,
    }

    return render(request, 'index.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})


def protagonist_detail(request, protagonist_name):
    # Get the protagonist object
    protagonist = get_object_or_404(Protagonist, name=protagonist_name)

    # Get all movies for this protagonist using the related_name 'movies'
    protagonist_movies = protagonist.movies.all().order_by('-upload_date')

    context = {
        'protagonist': protagonist,
        'movies': protagonist_movies,
    }

    return render(request, 'protagonist_detail.html', context)