from django.apps import AppConfig


class SuperheroesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'superheroes'
    verbose_name = "Супергерои мира"
