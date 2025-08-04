from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect


from django.shortcuts import redirect

class ProfileDataRequired:
    def dispatch(self, request, *args, **kwargs):
        profile = getattr(request.user, 'profile', None)
        if profile and profile.first_name and profile.last_name and profile.phone_number:
            return super().dispatch(request, *args, **kwargs)
        return redirect('edit_profile', pk=request.user.pk)  # Customize this as needed
class EditListingPermissionRequired:
    def dispatch(self, request, *args, **kwargs):
        if request.user.has_perm('offer.change_carlisting') or request.user.has_perm('offer.change_boatlisting') or request.user.has_perm('offer.change_motolisting'):
            print("YES HE HAS " ,request.user.has_perm('offer.change_carlisting'))
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied("You do not have permission to edit this listing.")