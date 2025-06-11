from django import forms
from .models import Book
from .models import Ebook

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['reg_no', 'program_title', 'date', 'services_required', 'auditorium_name', 'requestor_detail']

class EbookForm(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = [
            'sno',
            'book_title',
            'author',
            'isbn',
            'english_name',
            'year_of_publish',
            'publisher_name',
        ]
