# views.py
import json
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models.functions import TruncDate
from .models import Book, Ebook  # Ensure these models exist
from .forms import BookForm
from django.utils.safestring import mark_safe

def home(request):
    return render(request, 'home.html')

def auditorium(request):
    books = Book.objects.all()
    return render(request, 'books/auditorium.html', {'books': books})

def ebook(request):
    ebooks = Ebook.objects.all()
    return render(request, 'books/ebook.html', {'ebooks': ebooks})

def analyze_view(request):
    excluded_fields = ['id', 'sno']
    fields = [field.name for field in Book._meta.get_fields()
              if field.name not in excluded_fields and not field.is_relation]
    range_values = range(1, 6)
    return render(request, 'books/analyze1.html', {
        'fields': fields,
        'dataset_name': 'Auditorium Dataset',
        'range_values': range_values
    })

def analyze_ebooks(request):
    excluded_fields = ['id']
    fields = [field.name for field in Ebook._meta.get_fields()
              if field.name not in excluded_fields and not field.is_relation]
    range_values = range(1, 6)
    ebooks = list(Ebook.objects.all().values())
    return render(request, 'books/analyze2.html', {
        'fields': mark_safe(json.dumps(fields)),
        'dataset_name': 'EBook Dataset',
        'range_values': range_values,
        'data_json': mark_safe(json.dumps(ebooks)),
    })

def data_api(request):
    # Get parameters
    fields = request.GET.get('fields', '')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    from_year = request.GET.get('from_year')
    to_year = request.GET.get('to_year')
    year_param = request.GET.get('year')
    dataset_type = request.GET.get('dataset_type', 'auditorium')

    if not fields:
        return JsonResponse({'error': 'No fields specified'}, status=400)

    field_list = [f.strip() for f in fields.split(',') if f.strip()]

    # Map 'year' field requested by frontend to actual model field
    model_field_mapping = {
        'year': 'year_of_publish'
    }

    try:
        if dataset_type == 'ebook':
            queryset = Ebook.objects.all()

            # Handle year filtering if 'year' is requested
            if 'year' in field_list:
                filter_field = model_field_mapping.get('year', 'year_of_publish')
                if from_year and to_year:
                    queryset = queryset.filter(
                        **{
                            f'{filter_field}__gte': from_year,
                            f'{filter_field}__lte': to_year
                        }
                    )
                elif year_param:
                    queryset = queryset.filter(**{filter_field: year_param})

        else:
            queryset = Book.objects.all()

            # Handle date filtering if 'date' is requested
            if 'date' in field_list:
                if from_date and to_date:
                    try:
                        from_date_obj = datetime.strptime(from_date, '%Y-%m-%d').date()
                        to_date_obj = datetime.strptime(to_date, '%Y-%m-%d').date()
                        queryset = queryset.annotate(date_only=TruncDate('date')).filter(
                            date_only__range=(from_date_obj, to_date_obj)
                        )
                    except ValueError:
                        return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

            # Handle year filtering for Book model if 'year' is requested
            if 'year' in field_list:
                if from_year and to_year:
                    queryset = queryset.filter(
                        year__gte=from_year,
                        year__lte=to_year
                    )
                elif year_param:
                    queryset = queryset.filter(year=year_param)

        # Return only selected fields
        data = list(queryset.values(*field_list))
        return JsonResponse(data, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.date = datetime.now().date()
            book.save()
            return redirect('auditorium')
    else:
        form = BookForm()

    return render(request, 'books/add_books.html', {'form': form})