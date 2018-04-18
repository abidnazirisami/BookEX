from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('me/', views.showUserProfile, name='profile'),
    path('user/<username>/', views.showProfile, name='viewprofile'),
    path('edit/', views.editUserProfile, name='editprofile')
]
