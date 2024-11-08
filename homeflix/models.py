from django.db import models
from django.utils import timezone

def movie_upload_path(instance, filename):
    return f'movies/{instance.title}/{filename}'

def protagonist_image_path(instance, filename):
    return f'protagonists/{instance.protagonist}/{filename}'

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    protagonist = models.CharField(max_length=100, verbose_name='Protagonista')
    protagonist_image = models.ImageField(
        upload_to=protagonist_image_path,
        verbose_name='Foto do Protagonista',
        blank=True,  # Permite que o campo fique vazio
        null=True    # Permite valor nulo no banco de dados
    )
    movie_file = models.FileField(
        upload_to=movie_upload_path,
        verbose_name='Arquivo do Filme'
    )
    upload_date = models.DateTimeField(default=timezone.now, verbose_name='Data de Upload')
    description = models.TextField(blank=True, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['-upload_date']

    def __str__(self):
        return f'{self.title} - {self.protagonist}'

