from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail

# from django.http import HttpResponse
from .models import Band, Listing
from .forms import ContactUsForm, BandForm, ListingForm

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

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)

        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
        return render(request, 'listings/band_create.html', {'form': form})

def band_update(request, id):
    band = get_object_or_404(Band, id=id)
    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_create.html', {'form': form, 'update': True})

def about(request):
    return render(request, 'listings/about-us.html')

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})

def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)

        if form.is_valid():
            band = form.save()
            return redirect('listing-detail', band.id)
    else:
        form = ListingForm()
        return render(request, 'listings/listing_create.html', {'form': form})
    
def listing_update(request, id):
    listing = get_object_or_404(Listing, id=id)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request, 'listings/listing_create.html', {'form': form, 'update': True})

def contact(request):
    print(f"La méthode est : {request.method}")
    print(f"Les données sont : {request.POST}")
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data['name'] or 'anonyme'} from Merchex Contact Us form",
                message= form.cleaned_data['message'],
                from_email= form.cleaned_data['email'],
                recipient_list = ['admin@merchex.xyz']
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact-us.html', {'form': form})

def email_sent(request):
    return render(request, 'listings/email-sent.html')