from django.contrib import admin
from .models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'active')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'sold', 'year', 'type', 'band')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)