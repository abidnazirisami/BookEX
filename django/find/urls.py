from django.urls import path

from . import views


urlpatterns = [
    path('searchlist/', views.displayBooks, name='search_result'),
    path('search/', views.searchBook, name='searchbook'),
]
