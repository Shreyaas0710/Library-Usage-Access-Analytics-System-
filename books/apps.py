from django.apps import AppConfig

class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'  # Must match the folder name exactly
    label = 'books'  # Explicit label helps avoid conflicts