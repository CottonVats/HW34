

from django.contrib import admin
from django.urls import path, register_converter
from books import views
from books.converters import PubDateConverter

register_converter(PubDateConverter, 'date_converter')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.BookListView.as_view()),
    path('books/<date_converter:date>/', views.BookListView.as_view()),
]

