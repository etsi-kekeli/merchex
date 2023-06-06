"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=views.band_list),
    path('bands/', view=views.band_list, name='band-list'),
    path('bands/<int:id>/', view=views.band_detail, name='band-detail'),
    path('bands/listings/<int:id>/', view=views.band_listings, name='band-listings'),
    path('bands/add/', view=views.band_create, name='band-create'),
    path('bands/<int:id>/update/', view=views.band_update, name='band-update'),
    path('bands/<int:id>/delete/', view=views.band_delete, name='band-delete'),
    path('about-us', view=views.about),
    path('contact-us/', view=views.contact, name='contact'),
    path('email-sent/', view=views.email_sent, name='email-sent'),
    path('listings/', view=views.listing_list, name='listing-list'),
    path('listings/<int:id>', view=views.listing_detail, name='listing-detail'),
    path('listings/add/', view=views.listing_create, name='listing-create'),
    path('listings/<int:id>/update', view=views.listing_update, name='listing-update'),
    path('listings/<int:id>/delete', view=views.listing_delete, name='listing-delete'),
]
