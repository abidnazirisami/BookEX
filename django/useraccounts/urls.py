from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.showUserProfile, name='profile'),
    path('edit/', views.editUserProfile, name='editprofile')
]
