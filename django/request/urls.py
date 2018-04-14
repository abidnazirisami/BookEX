from django.urls import path

from . import views


urlpatterns = [
    path('requestlist/', views.displayList, name='request_result'),
    path('request/', views.searchBook, name='requestbook'),
]
