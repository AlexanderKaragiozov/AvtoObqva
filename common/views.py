from itertools import chain

from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView

from offer.forms import CarSearchForm, BoatSearchForm, MotoSearchForm
from offer.models import CarListing, BoatListing, MotoListing


# Create your views here.

class HomeView(ListView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_form'] = CarSearchForm()
        context['boat_form'] = BoatSearchForm()
        context['moto_form'] = MotoSearchForm()
        listings = self.get_queryset()
        if self.request.GET.get('form_type') == 'cars':
            context['listings'] = listings
            for car in listings:
                car.type = 'car'
            return  context
        elif self.request.GET.get('form_type') == 'boats':
            context['listings'] = listings
            for boat in listings:
                boat.type = 'boat'
            return context
        elif self.request.GET.get('form_type') == 'motos':
            context['listings'] = listings
            for moto in listings:
                moto.type = 'moto'
            return context
        else:
            boat_listings = BoatListing.objects.all()
            moto_listings = MotoListing.objects.all()
            all_listings = list(chain(listings, boat_listings, moto_listings))
            for listing in all_listings:
                if isinstance(listing, CarListing):
                    listing.type = "car"
                elif isinstance(listing, BoatListing):
                    listing.type = "boat"
                elif isinstance(listing, MotoListing):
                    listing.type = "moto"
            context['listings'] = all_listings
            return context
    def get_queryset(self):
        #Общи полета между 3-те форми
        form_type = self.request.GET.get('form_type')
        title = self.request.GET.get('title')
        category = self.request.GET.get('category')
        make = self.request.GET.get('make')
        year = self.request.GET.get('year')
        fuel_type = self.request.GET.get('fuel_type')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        location = self.request.GET.get('location')
        if form_type == 'cars':
            queryset = CarListing.objects.all()
            model = self.request.GET.get('model')
            kilometers = self.request.GET.get('kilometers')
            transmission = self.request.GET.get('transmission')
            horsepower = self.request.GET.get('horsepower')
            if title:
                queryset = queryset.filter(title__icontains=title)

            if make:
                queryset = queryset.filter(make__icontains=make)

            if year:
                queryset = queryset.filter(year=year)

            if fuel_type:
                queryset = queryset.filter(fuel_type__icontains=fuel_type)

            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
            if location:
                queryset = queryset.filter(location__icontains=location)
            if model:
                queryset = queryset.filter(model=model)
            if kilometers:
                queryset = queryset.filter(kilometers=kilometers)
            if transmission:
                queryset = queryset.filter(transmission=transmission)
            if horsepower:
                queryset = queryset.filter(horsepower=horsepower)
            return queryset


        elif form_type == 'boats':
            # Boat fields
            queryset = BoatListing.objects.all()
            if title:
                queryset = queryset.filter(title__icontains=title)

            if make:
                queryset = queryset.filter(make__icontains=make)

            if year:
                queryset = queryset.filter(year=year)

            if fuel_type:
                queryset = queryset.filter(type__icontains=fuel_type)

            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
            if location:
                queryset = queryset.filter(location__icontains=location)
            length = self.request.GET.get('length')
            material = self.request.GET.get('material')
            capacity = self.request.GET.get('capacity')
            horsepower = self.request.GET.get('horsepower')
            if length:
                queryset = queryset.filter(length__gte=length)
            if material:
                queryset = queryset.filter(material__icontains=material)
            if capacity:
                queryset = queryset.filter(capacity__gte=capacity)
            if horsepower:
                queryset = queryset.filter(horsepower__gte=horsepower)
            return queryset

        elif form_type == 'motos':
            # Moto fields
            queryset = MotoListing.objects.all()
            if title:
                queryset = queryset.filter(title__icontains=title)

            if make:
                queryset = queryset.filter(make__icontains=make)

            if year:
                queryset = queryset.filter(year=year)

            if fuel_type:
                queryset = queryset.filter(type__icontains=fuel_type)

            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
            if location:
                queryset = queryset.filter(location__icontains=location)
            engine_size = self.request.GET.get('engine_size')
            engine_type = self.request.GET.get('engine_type')
            if engine_size:
                queryset = queryset.filter(engine_size__gte=engine_size)
            if engine_type:
                queryset = queryset.filter(engine_type=engine_type)
            return queryset
        return CarListing.objects.all()

