from django.urls import path

from . import views


urlpatterns = [
    path('requestlist/', views.displayList, name='request_result'),
    path('', views.searchBook, name='requestbook'),
    path('success/', views.addToRequestQueue, name='display_wishlist'),
    path('wishlist/', views.showWishlist, name='wishlist')
]
