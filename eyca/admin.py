from django.contrib import admin
from eyca.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'college')


admin.site.register(Profile, ProfileAdmin)
