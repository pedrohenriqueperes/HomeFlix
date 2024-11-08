from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'protagonist', 'upload_date')  # Campos que aparecem na lista
    list_filter = ('upload_date',)  # Adiciona filtro por data
    search_fields = ('title', 'protagonist')  # Permite buscar por título e protagonista
    readonly_fields = ('upload_date',)  # Data de upload não pode ser editada
    fieldsets = (
        ('Informações Principais', {
            'fields': ('title', 'protagonist', 'protagonist_image')
        }),
        ('Arquivo', {
            'fields': ('movie_file', 'description')
        }),
        ('Informações Adicionais', {
            'fields': ('upload_date',)
        })
    )