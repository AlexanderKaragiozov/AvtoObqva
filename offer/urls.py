from django.urls.conf import path


from offer import views

urlpatterns = [
    path('add-car',views.CarListingCreateView.as_view(),name='add_car'),
    path('add-boat',views.BoatListingCreateView.as_view(),name='add_boat'),
    path('add-moto',views.MotoListingCreateView.as_view(),name='add_moto'),
    path('<int:pk>', views.ViewMyListings.as_view(), name='listings'),
    path('<str:table>/<int:pk>/edit', views.UpdateListing.as_view(), name='edit_listing'),
    path('<str:table>/<int:pk>/delete', views.DeleteListing.as_view(), name='delete_listing'),
    path('details/<str:table>/<int:pk>', views.ListingDetails.as_view(), name='details'),
    path('ask-ai/<str:make>/<str:model>/<str:year>/<str:horsepower>', views.ask_ai, name='ask_ai'),
]