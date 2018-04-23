from django.urls import path

from . import views


urlpatterns = [
    path('requestlist/', views.displayList, name='request_result'),
    path('', views.searchBook, name='requestbook'),
    path('success/', views.addToRequestQueue, name='display_wishlist'),
    path('wishlist/', views.showWishlist, name='wishlist'),
    path('addNew/', views.addNew, name='addNew'),
    path('wish/<req_isbn>/', views.addToWishlist, name='addtowishlist'),
    path('topRequest/', views.displayTopRequest, name = 'request_list'),
    path('pending/', views.pendingTransactions, name = 'pending'),
    path('cancelled', views.confirmWishRejection, name='confirm_wish_cancel'),
]
