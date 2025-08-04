from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect


from django.shortcuts import redirect

class ProfileDataRequired:
    def dispatch(self, request, *args, **kwargs):
        profile = getattr(request.user, 'profile', None)
        if profile and profile.first_name and profile.last_name and profile.phone_number:
            return super().dispatch(request, *args, **kwargs)
        return redirect('edit_profile', pk=request.user.pk)  # Customize this as needed
