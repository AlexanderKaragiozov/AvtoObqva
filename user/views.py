from urllib import request

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from user.Mixins import UserPassMixin
from user.forms import StyledLoginForm, StyledRegisterForm, ProfileForm
from user.models import Profile


# Create your views here.
class ProfileView( DetailView):
    template_name = 'profile.html'
    model = Profile
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_profile = Profile.objects.get(user=self.kwargs['pk'])
        context['can_edit'] = (
                current_profile.user == self.request.user or
                self.request.user.has_perm('offer.change_carlisting')
        )
        context['can_delete'] = (
                current_profile.user == self.request.user or
                self.request.user.has_perm('offer.delete_carlisting')
        )
        return context


class ProfileEditView(LoginRequiredMixin, UserPassMixin, UpdateView):
    template_name = 'edit-profile.html'
    model = Profile
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.kwargs['pk']})


    def get_object(self):
        return Profile.objects.get(user=self.kwargs['pk'])  # or use self.request.user.profile

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteProfileView(LoginRequiredMixin, UserPassMixin, DeleteView):
    template_name = 'delete-profile.html'
    model = User
    success_url = reverse_lazy('home')
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        user = self.object.user
        user.groups.clear()
        user.user_permissions.clear()
        user.delete()
        self.object.delete()
        return super().delete(request, *args, **kwargs)


class Login_View(LoginView):
    form_class = StyledLoginForm
    template_name = 'accounts/login.html'
class Register_View(CreateView):
    form_class = StyledRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')
