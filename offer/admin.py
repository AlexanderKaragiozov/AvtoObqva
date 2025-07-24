from django.contrib import admin

from offer.models import CarListing, BoatListing, MotoListing


# Register your models here.

@admin.register(CarListing)
class CarListingAdmin(admin.ModelAdmin):
    list_display =('title', 'make', 'model','price')
    list_filter = ('make',)
    search_fields = ('title', 'make', 'model')

@admin.register(BoatListing)
class BoatListingAdmin(admin.ModelAdmin):
    list_display =('title', 'make', 'year','price')
    list_filter = ('make',)
    search_fields = ('title', 'make', 'year')

@admin.register(MotoListing)
class MotoListingAdmin(admin.ModelAdmin):
    list_display =('title', 'make', 'year','price')
    list_filter = ('make',)
    search_fields = ('title', 'make', 'year')