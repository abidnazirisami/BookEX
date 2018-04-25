from django.urls import path

from . import views


urlpatterns = [
	path('', views.messages, name='messages'),
    path('mail/<receiver>', views.mail, name='mail'),
]
