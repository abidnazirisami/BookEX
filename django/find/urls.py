from django.urls import path

from . import views


urlpatterns = [
    path('searchlist/', views.displayBooks, name='search_result'),
    path('search/', views.searchBook, name='searchbook'),
    path('donate/', views.donate, name='donate'),
    path('search/addNew/', views.addNew, name='addNew'),
    path('donor/', views.displayTopDonor, name = 'donor_list'),
]
