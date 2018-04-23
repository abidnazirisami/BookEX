from django.urls import path

from . import views


urlpatterns = [
    path('rate/<isbn>', views.rate, name='rate'),
]

