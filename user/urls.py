from django.urls.conf import path

from user import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('<int:pk>/edit', views.ProfileEditView.as_view(), name='edit_profile'),
    path('<int:pk>/delete', views.DeleteProfileView.as_view(), name='delete_profile'),
    path('register/', views.Register_View.as_view(), name='register'),
    path('login/', views.Login_View.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]