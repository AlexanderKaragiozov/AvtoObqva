from django.contrib import admin

from user.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name')
    list_filter = ('user',)
    search_fields = ('user__username', 'first_name', 'last_name')
    ordering = ('user',)


