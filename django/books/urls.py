from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.displayBooks, name='list_of_books'),
    path('donate/', views.addBook, name='addbook'),
    path('addNew/',views.addNew,name='addNew'),
    path('details/<req_isbn>/', views.viewBookProfile, name='viewbookprofile'),
]
