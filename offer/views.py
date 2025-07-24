from django.urls import reverse_lazy
from django.forms.models import ModelForm
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.safestring import mark_safe

import offer,markdown
from offer.ai_ask_request import run_ollama
from offer.forms import CarListingCreationForm,BoatListingCreationForm,MotoListingCreationForm
from offer.models import CarListing, BoatListing, MotoListing
from user.Mixins import UserPassMixin,DeleteListingMixin
from user.models import Profile


# Create your views here.

# class AddListingView(CreateView):
#     template_name = 'add-listing.html'

# def add_car(request):
#
#     context = {
#         "car":True
#     }
#     ## PROBLEMA E V JAVASCRIPTA
#     return render(request,'common/car.html',context)

class CarListingCreateView(LoginRequiredMixin,CreateView):
    model = offer.models.CarListing
    form_class = CarListingCreationForm
    template_name = "common/car.html"

    def get_success_url(self):
        return reverse_lazy('listings', kwargs={'pk': self.request.user.pk})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = True
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)


        return response

class BoatListingCreateView(CreateView,LoginRequiredMixin):
    model = offer.models.BoatListing
    form_class = BoatListingCreationForm
    template_name = "common/boat.html"

    def get_success_url(self):
        return reverse_lazy('listings', kwargs={'pk': self.request.user.pk})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['boat'] = True
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)


        return response

class MotoListingCreateView(CreateView,LoginRequiredMixin):
    model = offer.models.MotoListing
    form_class = MotoListingCreationForm
    template_name = "common/moto.html"

    def get_success_url(self):
        return reverse_lazy('listings', kwargs={'pk': self.request.user.pk})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['moto'] = True
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)


        return response

class ViewMyListings(ListView):
    template_name = 'my-listings.html'

    def get_queryset(self):
        car_set = CarListing.objects.filter(owner=self.kwargs['pk'])


        return car_set
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_listings'] = self.get_queryset()

        context['boat_listings'] = BoatListing.objects.filter(owner=self.kwargs['pk'])

        context['moto_listings'] = MotoListing.objects.filter(owner=self.kwargs['pk'])

        if context['car_listings'] or context['boat_listings'] or context['moto_listings']:
            context['has_listings'] = True
        else:
            context['has_listings'] = False
        current_profile = Profile.objects.get(user=self.kwargs['pk'])
        context['can_edit'] = (
                current_profile.user == self.request.user or
                self.request.user.has_perm('offer.change_carlisting')
        )
        context['can_delete'] = (
                current_profile.user == self.request.user or
                self.request.user.has_perm('offer.delete_carlisting')
        )
        context['listing_owner'] = Profile.objects.get(pk=self.kwargs['pk']).user.username
        return context


class ListingDetails(DetailView):

    def get(self,request,table,pk):
        if table == 'cars':
            self.object = CarListing.objects.get(pk=pk)
            self.object.type = 'car'
            self.object.views += 1
            self.object.save()
            context = self.get_context_data()
            context['vehicle'] = self.object
            return render(request,'listing-details.html',context)
        elif table == 'boats':
            self.object = BoatListing.objects.get(pk=pk)
            self.object.type = 'boat'
            self.object.views += 1
            self.object.save()
            context = self.get_context_data()
            context['vehicle'] = self.object
            return render(request,'listing-details.html',context)
        elif table == 'motos':
            self.object = MotoListing.objects.get(pk=pk)
            self.object.type = 'moto'
            self.object.views += 1
            self.object.save(update_fields=['views'])
            context = self.get_context_data()
            context['vehicle'] = self.object
            return render(request,'listing-details.html',context)

class UpdateListing(LoginRequiredMixin, UserPassMixin, UpdateView):


    template_name = "edit-listing.html"
    def get_success_url(self):
        return reverse_lazy('listings', kwargs={'pk': self.request.user.pk})
    def get_object(self):
        table = self.kwargs['table']
        if table == 'car':
            car = CarListing.objects.get(pk=self.kwargs['pk'])
            car.type = 'car'
            return car
        elif table == 'boat':
            boat = BoatListing.objects.get(pk=self.kwargs['pk'])
            boat.type = 'boat'
            return boat
        elif table =='moto':
            moto = MotoListing.objects.get(pk=self.kwargs['pk'])
            moto.type = 'moto'
            return moto
    def get_form_class(self):
        if self.object.type == 'car':
            return CarListingCreationForm
        elif self.object.type == 'boat':
            return BoatListingCreationForm
        elif self.object.type == 'moto':
            return MotoListingCreationForm


class DeleteListing(LoginRequiredMixin, DeleteListingMixin, DeleteView):

    def get_model(self):
        table = self.kwargs.get('table')
        if table == 'car':
            return CarListing
        elif table == 'boat':
            return BoatListing
        elif table == 'moto':
            return MotoListing

    def get_queryset(self):
        self.model = self.get_model()
        return self.model.objects.filter(pk=self.kwargs['pk'])

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')











def ask_ai(request, make, model, year, horsepower):
    response = run_ollama(make, model, year, horsepower)
    raw_text = response.get('response', '')

    # Convert Markdown to HTML (this removes the stars and formats bold properly)
    html = markdown.markdown(raw_text)

    # Now improve structure by injecting headings for the numbered sections
    # Use regex to replace the numbers followed by dot and a space, with <h4> heading tags
    import re

    def repl_heading(match):
        num = match.group(1)
        titles = {
            "1": "Надеждност",
            "2": "Често срещани проблеми / Известни дефекти",
            "3": "Трансмисия",
            "4": "Въздействие върху околната среда",
            "5": "Разход на гориво",
            "6": "Безопасност",
            "7": "Разходи за поддръжка",
        }
        title = titles.get(num, "")
        return f'</p><h4>{num}. {title}</h4><p>'

    # Wrap whole html in <p> to handle first replacement properly
    html = "<p>" + html + "</p>"

    # Replace the numbered points headings with formatted ones
    html = re.sub(r'</p><p>\s*([1-7])\.\s*', repl_heading, html)

    # Clean any empty paragraphs from the start/end if necessary
    html = re.sub(r'^(<p>\s*</p>)+', '', html)
    html = re.sub(r'(<p>\s*</p>)+$', '', html)

    # Mark as safe for Django template
    safe_html = mark_safe(html)

    messages.success(request, safe_html)
    return redirect(request.META.get("HTTP_REFERER", "/"))