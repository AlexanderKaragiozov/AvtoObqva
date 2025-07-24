import django.urls as urls
from django.urls.conf import path

import common.views

urlpatterns = [
    path('', common.views.HomeView.as_view(), name='home'),
]