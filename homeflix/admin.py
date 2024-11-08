from django.contrib import admin
from .models import Movie, Protagonist


@admin.register(Protagonist)
class ProtagonistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_protagonist_name', 'upload_date')
    list_filter = ('upload_date', 'protagonist')
    search_fields = ('title', 'protagonist__name')
    readonly_fields = ('upload_date',)

    fieldsets = (
        ('Informações Principais', {
            'fields': ('title', 'protagonist')
        }),
        ('Arquivo', {
            'fields': ('movie_file', 'description')
        }),
        ('Informações Adicionais', {
            'fields': ('upload_date',)
        })
    )

    def get_protagonist_name(self, obj):
        return obj.protagonist.name

    get_protagonist_name.short_description = 'Protagonista'
    get_protagonist_name.admin_order_field = 'protagonist__name'