from django.urls import path

from . import views

urlpatterns = [
    path('', views.displayTable, name='test'),
]