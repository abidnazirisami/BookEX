from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.displayBooks, name='list_of_books'),
    path('donate/', views.addBook, name='addbook'),
]