from django.contrib.auth.mixins import UserPassesTestMixin
from offer.models import CarListing, BoatListing, MotoListing
from user.models import Profile


class UserPassMixin(UserPassesTestMixin):
    def test_func(self):
        try:
            profile = Profile.objects.get(pk=self.request.user.pk)

            if self.request.user == profile.user:
                return True
        except Profile.DoesNotExist:
            pass



        if self.request.user.has_perm('offer.change_carlisting'):
            return True



class DeleteListingMixin(UserPassesTestMixin):
    def test_func(self):
        table = self.kwargs['table']
        pk = self.kwargs['pk']
        vehicle = None
        if table == 'car':
            vehicle = CarListing.objects.get(pk=pk)
        elif table == 'boat':
            vehicle = BoatListing.objects.get(pk=pk)
        elif table == 'moto':
            vehicle = MotoListing.objects.get(pk=pk)

        if vehicle.owner == self.request.user:
            return True
        if self.request.user.is_superuser:
            return True