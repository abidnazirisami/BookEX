"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('storyOfUs', views.story, name='story'),
    path('confirmed', views.confirmDonation, name='confirm_donation'),
    path('cancelled', views.confirmRejection, name='confirm_rejection'),
    path('cancellDonation', views.dontDonate, name='donation_cancel'),
    path('donated', views.donate, name='donate_final'),
    path('aboutUs', TemplateView.as_view(template_name='about.html'), name='aboutUs'),
    path('contactUs', views.contact, name='contact'),
    path('profile/', include('useraccounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('pages/', include('pages.urls')),
    path('book/', include('books.urls')),
    path('find/', include('find.urls')),
    path('request/', include('request.urls')),
    path('rating/', include('rating.urls')),
    path('message/', include('mail.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
