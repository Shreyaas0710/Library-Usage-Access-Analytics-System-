from django.contrib import admin
from .models import Book
from .models import Ebook

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'sno',
        'reg_no',
        'program_title',
        'date',
        'services_required',
        'auditorium_name',
        'requestor_detail'
    )
    list_filter = ('auditorium_name',)

@admin.register(Ebook)
class EBookAdmin(admin.ModelAdmin):
    list_display = ('sno', 'book_title', 'author', 'isbn', 'english_name', 'year_of_publish', 'publisher_name')
    search_fields = ('title', 'author', 'isbn', 'publisher_name','english_name')