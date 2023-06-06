from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from .models import Band, Listing

# Create your views here.

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands' : bands})

def band_detail(request, id):
    band = get_object_or_404(Band, id=id)
    return render(request, 'listings/band_detail.html', {'band': band})

def band_listings(request, id):
    band = get_object_or_404(Band, id=id)
    listings = band.listing_set.all()
    print(listings)
    return render(request, 'listings/listing_list.html', {'listings': listings})

def about(request):
    return render(request, 'listings/about-us.html')

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})

def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, 'listings/listing_detail', {'listing': listing})

def contact(request):
    return render(request, 'listings/contact-us.html')