from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auditorium/', views.auditorium, name='auditorium'),
    path('ebook/', views.ebook, name='ebook'),
    path('ebook/analyze/', views.analyze_ebooks, name='analyze_ebook'),  # your analyze ebooks page
    path('analyze1/', views.analyze_view, name='analyze1'),
    path('analyze2/', views.analyze_view, name='analyze2'),
    path('api/data/', views.data_api, name='data_api'),
    path('add/', views.add_book, name='add_book'),
]